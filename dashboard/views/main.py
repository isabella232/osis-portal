##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2016 Université catholique de Louvain (http://www.uclouvain.be)
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
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from base.views import layout
from attribution.utils import permission


@login_required
def home(request):
    return layout.render(request, "dashboard.html", {
        'online_application_opened': permission.is_online_application_opened(request.user),
        'manage_courses_url': settings.OSIS_MANAGE_COURSES_URL,
        'osis_vpn_help_url': settings.OSIS_VPN_HELP_URL
    })


@login_required
def faculty_administration(request):
    if not _can_access_administration(request):
        raise PermissionDenied
    return layout.render(request, "faculty_administrator_dashboard.html",
                         {'online_application_opened': permission.is_online_application_opened(request.user)})


def show_multiple_registration_id_error(request):
    msg = _("A problem was detected with your registration : 2 registration id's are linked to your user. Please "
            "contact the registration departement (SIC). Thank you.")
    messages.add_message(request, messages.ERROR, msg)
    return home(request)


def _can_access_administration(request):
    if request.user.has_perm('base.is_faculty_administrator'):
        return True
    can_access = False
    if 'performance' in settings.INSTALLED_APPS:
        from performance.views import main as perf_main_view
        can_access = perf_main_view.__can_access_performance_administration(request)
    return can_access
