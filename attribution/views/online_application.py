##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2021 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, FormView

from attribution.business import tutor_application
from attribution.calendar.application_courses_calendar import ApplicationCoursesRemoteCalendar
from attribution.forms.application import ApplicationForm, VacantAttributionFilterForm
from attribution.services.application import ApplicationService
from attribution.services.attribution import AttributionService
from attribution.utils import permission
from base import models as mdl_base
from base.forms.base_forms import GlobalIdForm
from base.models.tutor import Tutor
from base.templatetags.academic_year_display import display_as_academic_year
from base.views import layout


logger = logging.getLogger(settings.DEFAULT_LOGGER)


@login_required
@permission_required('attribution.can_access_attribution_application', raise_exception=True)
def outside_period(request):
    calendar = ApplicationCoursesRemoteCalendar()
    if calendar.get_opened_academic_events():
        return HttpResponseRedirect(reverse('applications_overview'))

    previous_academic_event = calendar.get_previous_academic_event()
    if previous_academic_event:
        messages.add_message(
            request,
            messages.WARNING,
            _('The period of online application for courses %(year)s opened on %(start_date)s to %(end_date)s') % {
                'year': display_as_academic_year(previous_academic_event.authorized_target_year),
                'start_date': previous_academic_event.start_date.strftime('%d/%m/%Y'),
                'end_date': previous_academic_event.end_date.strftime('%d/%m/%Y')
                if previous_academic_event.end_date else ''
            }
        )

    next_academic_event = calendar.get_next_academic_event()
    if next_academic_event:
        messages.add_message(
            request,
            messages.WARNING,
            _('The period of online application for courses %(year)s will open on %(start_date)s to %(end_date)s') % {
                'year': display_as_academic_year(next_academic_event.authorized_target_year),
                'start_date': next_academic_event.start_date.strftime('%d/%m/%Y'),
                'end_date': next_academic_event.end_date.strftime('%d/%m/%Y') if next_academic_event.end_date else ''
            }
        )
    return layout.render(request, "attribution_access_denied.html", {})


@login_required
@permission_required('base.is_faculty_administrator', raise_exception=True)
@require_http_methods(["GET", "POST"])
def administration_applications(request):
    if request.method == "POST":
        form = GlobalIdForm(request.POST)
        if form.is_valid():
            global_id = form.cleaned_data['global_id']
            return redirect('visualize_tutor_applications', global_id=global_id)
    else:
        form = GlobalIdForm()
    return layout.render(request, "admin/applications_administration.html", {"form": form})


class ApplicationOverviewView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    # PermissionRequiredMixin
    permission_required = "attribution.can_access_attribution_application"
    raise_exception = True

    # TemplateView
    template_name = "attribution_overview.html"

    def get(self, request, *args, **kwargs):
        if not permission.is_online_application_opened(self.request.user):
            return redirect("outside_applications_period")
        return super().get(request, *args, **kwargs)

    @cached_property
    def tutor(self):
        return self.request.user.person.tutor

    @cached_property
    def application_course_calendar(self):
        calendars = ApplicationCoursesRemoteCalendar().get_opened_academic_events()
        if len(calendars) > 1:
            logger.warning("Multiple application courses calendars opened at same time")
        return calendars[0]

    @cached_property
    def applications(self):
        return ApplicationService.get_applications(self.tutor.person)

    @cached_property
    def attributions_about_to_expire(self):
        return ApplicationService.get_attribution_about_to_expires(self.tutor.person)

    @cached_property
    def attributions_of_application_year(self):
        application_course_year = self.application_course_calendar.authorized_target_year
        return AttributionService.get_attributions_list(application_course_year, self.tutor.person)

    def get_total_lecturing_charge(self):
        return sum(
            [
                float(attribution.lecturing_charge) if attribution.lecturing_charge else 0
                for attribution in self.attributions_of_application_year
            ]
        )

    def get_total_practical_charge(self):
        return sum(
            [
                float(attribution.practical_charge) if attribution.practical_charge else 0
                for attribution in self.attributions_of_application_year
            ]
        )

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(),
            'application_course_calendar': self.application_course_calendar,
            'attributions_about_to_expire': self.attributions_about_to_expire,
            'attributions': self.attributions_of_application_year,
            'tot_lecturing': self.get_total_lecturing_charge(),
            'tot_practical': self.get_total_practical_charge(),
            'applications': self.applications,
            'application_academic_year': display_as_academic_year(
                self.application_course_calendar.authorized_target_year
            ),
            'previous_academic_year': display_as_academic_year(
                self.application_course_calendar.authorized_target_year - 1
            ),
            'a_tutor': self.tutor,
            'catalog_url': settings.ATTRIBUTION_CONFIG.get('CATALOG_URL'),
            'help_button_url': settings.ATTRIBUTION_CONFIG.get('HELP_BUTTON_URL'),
        }


class ApplicationOverviewAdminView(ApplicationOverviewView):
    permission_required = "base.is_faculty_administrator"

    @cached_property
    def tutor(self):
        return Tutor.objects.filter(person__global_id=self.kwargs['global_id'])


class SearchVacantCoursesView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    # PermissionRequiredMixin
    permission_required = "attribution.can_access_attribution_application"
    raise_exception = True

    # TemplateView
    template_name = "attribution_vacant_list.html"

    @cached_property
    def tutor(self):
        return self.request.user.person.tutor

    def get(self, request, *args, **kwargs):
        if not permission.is_online_application_opened(self.request.user):
            return redirect("outside_applications_period")

        form = VacantAttributionFilterForm(data=request.GET)
        if request.GET and form.is_valid():
            kwargs['vacant_courses'] = ApplicationService.search_vacant_courses(
                code=form.cleaned_data['learning_container_acronym'],
                allocation_faculty=getattr(form.cleaned_data['faculty'], 'acronym', ''),
                person=self.tutor.person
            )
        kwargs['form'] = form
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'a_tutor': self.tutor,
            'help_button_url': settings.ATTRIBUTION_CONFIG.get('HELP_BUTTON_URL'),
        }


class CreateApplicationView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    # PermissionRequiredMixin
    permission_required = "attribution.can_access_attribution_application"
    raise_exception = True

    # FormView
    form_class = ApplicationForm
    template_name = "application_form.html"

    @cached_property
    def tutor(self):
        return self.request.user.person.tutor

    @cached_property
    def vacant_course(self):
        return ApplicationService.get_vacant_course(code=self.kwargs['vacant_course_code'], person=self.tutor.person)

    def get(self, request, *args, **kwargs):
        if not permission.is_online_application_opened(self.request.user):
            return redirect("outside_applications_period")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not permission.is_online_application_opened(self.request.user):
            return redirect("outside_applications_period")
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        return {
            **super().get_form_kwargs(),
            'vacant_course': self.vacant_course
        }

    def form_valid(self, form):
        response = ApplicationService.create_application(
            vacant_course_code=self.kwargs['vacant_course_code'],
            lecturing_volume=form.cleaned_data['charge_lecturing_asked'],
            practical_volume=form.cleaned_data['charge_practical_asked'],
            remark=form.cleaned_data['remark'],
            course_summary=form.cleaned_data['course_summary'],
            person=self.tutor.person
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'save_url': reverse('create_application', kwargs={'vacant_course_code': self.kwargs['vacant_course_code']}),
            'cancel_url': reverse('applications_overview'),
            'a_tutor': self.tutor,
            'help_button_url': settings.ATTRIBUTION_CONFIG.get('HELP_BUTTON_URL'),
        }

    def get_success_url(self):
        return reverse('applications_overview')


class UpdateApplicationView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    # PermissionRequiredMixin
    permission_required = "attribution.can_access_attribution_application"
    raise_exception = True

    # FormView
    form_class = ApplicationForm
    template_name = "application_form.html"

    @cached_property
    def tutor(self):
        return self.request.user.person.tutor

    @cached_property
    def application(self):
        return ApplicationService.get_application(self.kwargs['application_uuid'], self.tutor.person)

    @cached_property
    def vacant_course(self):
        return ApplicationService.get_vacant_course(code=self.application.code, person=self.tutor.person)

    def get(self, request, *args, **kwargs):
        if not permission.is_online_application_opened(self.request.user):
            return redirect("outside_applications_period")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not permission.is_online_application_opened(self.request.user):
            return redirect("outside_applications_period")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = ApplicationService.update_application(
            application_uuid=self.kwargs['application_uuid'],
            lecturing_volume=form.cleaned_data['charge_lecturing_asked'],
            practical_volume=form.cleaned_data['charge_practical_asked'],
            remark=form.cleaned_data['remark'],
            course_summary=form.cleaned_data['course_summary'],
            person=self.tutor.person
        )
        return super().form_valid(form)

    def get_initial(self):
        return self.application

    def get_form_kwargs(self):
        return {
            **super().get_form_kwargs(),
            'vacant_course': self.vacant_course
        }

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'save_url': reverse('update_application', kwargs={'application_uuid': self.kwargs['application_uuid']}),
            'cancel_url': reverse('applications_overview'),
            'a_tutor': self.tutor,
            'help_button_url': settings.ATTRIBUTION_CONFIG.get('HELP_BUTTON_URL'),
        }

    def get_success_url(self):
        return reverse('applications_overview')


class RenewMultipleAttributionsAboutToExpireView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # PermissionRequiredMixin
    permission_required = "attribution.can_access_attribution_application"
    raise_exception = True

    def post(self, request, *args, **kwargs):
        if not permission.is_online_application_opened(self.request.user):
            return redirect("outside_applications_period")

        post_data = dict(request.POST.lists())
        vacant_course_codes = [
            param.split("_")[-1] for param, value in post_data.items() if "vacant_course_" in param
        ]

        if vacant_course_codes:
            ApplicationService.renew_attributions_about_to_expire(vacant_course_codes, self.request.user.person)
        else:
            messages.add_message(request, messages.ERROR, _('No attribution renewed'))
        return redirect('applications_overview')


class DeleteApplicationView(LoginRequiredMixin, PermissionRequiredMixin, View):
    # PermissionRequiredMixin
    permission_required = "attribution.can_access_attribution_application"
    raise_exception = True

    def post(self, request, *args, **kwargs):
        if not permission.is_online_application_opened(self.request.user):
            return redirect("outside_applications_period")

        ApplicationService.delete_application(self.kwargs['application_uuid'], self.request.user.person)
        return redirect('applications_overview')


@login_required
@permission_required('attribution.can_access_attribution_application', raise_exception=True)
@require_http_methods(["POST"])
@user_passes_test(permission.is_online_application_opened, login_url=reverse_lazy('outside_applications_period'))
def send_mail_applications_summary(request):
    tutor = mdl_base.tutor.find_by_user(request.user)
    global_id = tutor.person.global_id
    error_msg = tutor_application.send_mail_applications_summary(global_id)
    if error_msg:
        messages.add_message(request, messages.ERROR, _(error_msg))
    else:
        messages.add_message(request, messages.INFO, _('An email with your applications have been sent'))
    return redirect('applications_overview')
