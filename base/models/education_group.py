##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2018 Université catholique de Louvain (http://www.uclouvain.be)
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
from django.db import models

from base.models.offer_enrollment import OfferEnrollment
from osis_common.models.serializable_model import SerializableModelAdmin, SerializableModel


class EducationGroupAdmin(SerializableModelAdmin):
    list_display = ('most_recent_acronym',)
    search_fields = ('educationgroupyear__acronym',)


class EducationGroup(SerializableModel):
    external_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.uuid)

    @property
    def most_recent_acronym(self):
        qs = self.educationgroupyear_set.all()
        if qs:
            most_recent_education_group = qs.latest('academic_year__year')
            return most_recent_education_group.acronym
        return None


def find_by_student_and_enrollment_states(student, offer_enrollment_states):
    educ_goup_ids = OfferEnrollment.objects.filter(
        student=student,
        enrollment_state__in=offer_enrollment_states
    ).values('education_group_year__education_group_id')
    return EducationGroup.objects.filter(pk__in=educ_goup_ids)
