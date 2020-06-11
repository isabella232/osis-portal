# -*- coding: utf-8 -*-
############################################################################
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
############################################################################
import json
import logging

from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied, MultipleObjectsReturned
from django.shortcuts import redirect
from django.utils.translation import ugettext as _

from base.forms.base_forms import RegistrationIdForm
from base.models import student as mdl_student
from base.views import layout, common
from dashboard.views import main as dash_main_view
from exam_enrollment.models.exam_enrollment_request import ExamEnrollmentRequest
from osis_common.utils.models import get_object_or_none
from performance import models as mdl_performance
from performance.models.enums import offer_registration_state

logger = logging.getLogger(settings.DEFAULT_LOGGER)


# Students Views

@login_required
@permission_required('base.is_student', raise_exception=True)
def view_performance_home(request):
    """
    Display the academic programs of the student.
    """
    try:
        stud = mdl_student.find_by_user(request.user)
    except MultipleObjectsReturned:
        return dash_main_view.show_multiple_registration_id_error(request)
    list_student_programs = None
    if stud:
        list_student_programs = __get_student_programs(stud)

    data = {
        "student": stud,
        "programs": list_student_programs,
        "registration_states_to_show": offer_registration_state.STATES_TO_SHOW_ON_PAGE
    }
    return layout.render(request, "performance_home_student.html", data)


def __make_not_authorized_message(stud_perf):
    authorized = stud_perf.authorized if stud_perf else None
    session_month = stud_perf.get_session_locked_display() if stud_perf else None
    if not authorized and session_month:
        return _('The publication of the notes from the %(session_month)s session was not authorized by our faculty.') \
               % {"session_month": session_month}
    else:
        return None


def __get_performance_data(stud_perf, stud=None):
    document = json.dumps(stud_perf.data) if stud_perf else None
    creation_date = stud_perf.creation_date if stud_perf else None
    update_date = stud_perf.update_date if stud_perf else None
    fetch_timed_out = stud_perf.fetch_timed_out if stud_perf else None
    not_authorized_message = __make_not_authorized_message(stud_perf)
    courses_registration_validated = stud_perf.courses_registration_validated if stud_perf else None
    learning_units_outside_catalog = stud_perf.learning_units_outside_catalog if stud_perf else None
    course_registration_message = stud_perf.course_registration_message if stud_perf else None
    session_month = stud_perf.get_session_locked_display() if stud_perf else None
    data = {}
    if stud_perf and stud:
        data = _get_exam_location_choices(stud, stud_perf)

    return {
        "results": document,
        "creation_date": creation_date,
        "update_date": update_date,
        "fetch_timed_out": fetch_timed_out,
        "not_authorized_message": not_authorized_message,
        "courses_registration_validated": courses_registration_validated,
        "learning_units_outside_catalog": learning_units_outside_catalog,
        "course_registration_message": course_registration_message,
        "session_month": session_month or '',
        'testwe_exam': data.get('testwe_exam') or '-',
        'teams_exam': data.get('teams_exam') or '-',
        'moodle_exam': data.get('moodle_exam') or '-',
        'covid_period': data.get('covid_period')
    }


def _get_exam_location_choices(stud, stud_perf):
    data = {}
    exam_enroll_request = get_object_or_none(
        ExamEnrollmentRequest,
        student=stud,
        offer_year_acronym=stud_perf.acronym
    )
    if exam_enroll_request:
        try:
            data = json.loads(exam_enroll_request.document)
        except json.JSONDecodeError:
            logger.exception("Json data is not valid")
            data = {}
    return data


@login_required
@permission_required('base.is_student', raise_exception=True)
def display_result_for_specific_student_performance(request, pk):
    """
    Display the student result for a particular year and program.
    """
    try:
        stud = mdl_student.find_by_user(request.user)
    except MultipleObjectsReturned:
        return dash_main_view.show_multiple_registration_id_error(request)
    stud_perf = mdl_performance.student_performance.find_actual_by_pk(pk)
    if not check_right_access(stud_perf, stud):
        raise PermissionDenied

    perf_data = __get_performance_data(stud_perf, stud)
    return layout.render(request,
                         "performance_result_student.html",
                         perf_data)


def _clean_acronym(acronym):
    if acronym:
        cleaned_acronym = str(acronym).replace("_", "/").upper()
        return cleaned_acronym
    return None


@login_required
@permission_required('base.is_student', raise_exception=True)
def display_results_by_acronym_and_year(request, acronym, academic_year):
    """
    Display the result for a students , filter by acronym
    """
    try:
        stud = mdl_student.find_by_user(request.user)
    except MultipleObjectsReturned:
        return dash_main_view.show_multiple_registration_id_error(request)
    cleaned_acronym = _clean_acronym(acronym)
    stud_perf = mdl_performance.student_performance.find_actual_by_student_and_offer_year(stud.registration_id,
                                                                                          academic_year,
                                                                                          cleaned_acronym)
    if not check_right_access(stud_perf, stud):
        raise PermissionDenied
    perf_data = __get_performance_data(stud_perf, stud)

    return layout.render(request,
                         "performance_result_student.html",
                         perf_data)


# Admins Views

@login_required
def select_student(request):
    """
    View to select a student to visualize his/her results.
    !!! Should only be accessible for staff having the rights.
    """
    if not __can_access_performance_administration(request):
        raise PermissionDenied
    if request.method == "POST":
        form = RegistrationIdForm(request.POST)
        if form.is_valid():
            registration_id = form.cleaned_data['registration_id']
            return redirect(visualize_student_programs, registration_id=registration_id)
    else:
        form = RegistrationIdForm()
    return layout.render(request, "admin/performance_administration.html", {"form": form})


@login_required
def visualize_student_programs(request, registration_id):
    """
    View to visualize a particular student list of academic programs.
    !!! Should only be accessible for staff having the rights.
    """
    if not __can_access_performance_administration(request):
        raise PermissionDenied
    stud = mdl_student.find_by_registration_id(registration_id)
    list_student_programs = None
    if stud:
        if not __can_visualize_student_programs(request, registration_id):
            raise PermissionDenied
        list_student_programs = __get_student_programs(stud)

    data = {
        "student": stud,
        "programs": list_student_programs,
        "registration_states_to_show": offer_registration_state.STATES_TO_SHOW_ON_PAGE
    }
    return layout.render(request, "admin/performance_home_admin.html", data)


@login_required
def visualize_student_result(request, pk):
    """
    View to visualize a particular student program courses result.
    !!! Should only be accessible for staff having the rights.
    """
    if not __can_access_performance_administration(request):
        raise PermissionDenied
    stud_perf = mdl_performance.student_performance.find_actual_by_pk(pk)
    if stud_perf and not __can_visualize_student_result(request, pk):
        raise PermissionDenied
    perf_data = __get_performance_data(stud_perf)
    return layout.render(request,
                         "admin/performance_result_admin.html",
                         perf_data)


def __get_student_programs(stud):
    query_result = mdl_performance.student_performance.search(registration_id=stud.registration_id)
    list_student_programs = query_result_to_list(query_result)
    return list_student_programs


def query_result_to_list(query_result):
    performance_results_list = []
    for row in query_result:
        performance_dict = convert_student_performance_to_dic(row)
        allowed_registration_states = [value for key, value in offer_registration_state.OFFER_REGISTRAION_STATES]
        if performance_dict and performance_dict.get("offer_registration_state") in allowed_registration_states:
            performance_results_list.append(performance_dict)
    return performance_results_list


def convert_student_performance_to_dic(student_performance_obj):
    d = dict()
    try:
        d["academic_year"] = student_performance_obj.academic_year_template_formated
        d["acronym"] = student_performance_obj.acronym
        d["title"] = json.loads(json.dumps(student_performance_obj.data))["monAnnee"]["monOffre"]["offre"][
            "intituleComplet"]
        d["pk"] = student_performance_obj.pk
        d["offer_registration_state"] = student_performance_obj.offer_registration_state
    except Exception:
        d = None
    return d


def check_right_access(student_performance, student):
    return student_performance and student and student_performance.registration_id == student.registration_id


def __can_visualize_student_programs(request, registration_id):
    """
    Student cannot access administration
    User can visualize student programs if :
        - The user is faculty_administrator
        - The user is program manager of at least one of the program in the list of the student programs
    """
    if request.user.has_perm('base.is_faculty_administrator'):
        return True
    if request.user.has_perm('base.is_student'):
        return False
    managed_programs_as_dict = common.get_managed_program_as_dict(request.user)
    for stud_perfs in mdl_performance.student_performance.search(registration_id=registration_id):
        if stud_perfs.acronym in managed_programs_as_dict.get(stud_perfs.academic_year, []):
            return True
    return False


def __can_visualize_student_result(request, performance_result_pk):
    """
    Student cannot access administration
    User can visualize the student result if :
        - The user is faculty_administrator
        - The user is program manager of the requested program
    """
    if request.user.has_perm('base.is_faculty_administrator'):
        return True
    if request.user.has_perm('base.is_student'):
        return False
    student_performance = mdl_performance.student_performance.find_actual_by_pk(performance_result_pk)
    if student_performance:
        managed_programs_as_dict = common.get_managed_program_as_dict(request.user)
        return student_performance.acronym in managed_programs_as_dict.get(student_performance.academic_year, [])
    return False


def __can_access_performance_administration(request):
    """
    Student cannot access administration
    User can access performance results administration if :
        - The user is faculty_administrator
        - The user is program manager of at least one program
    """
    return request.user.has_perm('base.is_faculty_administrator') or (
            not request.user.has_perm('base.is_student') and bool(common.get_managed_program_as_dict(request.user))
    )
