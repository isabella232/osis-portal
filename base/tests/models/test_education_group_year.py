##############################################################################
#
# OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2018-2019 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
import datetime

from django.test import TestCase

from base.models import education_group_year
from base.tests.factories.academic_year import AcademicYearFactory
from base.tests.factories.education_group import EducationGroupFactory
from base.tests.factories.education_group_year import EducationGroupYearFactory



class TestEducationGroupYear(TestCase):
    def setUp(self):
        self.education_group = EducationGroupFactory()
        now = datetime.date.today()
        a_year = now.year
        self.curent_academic_year = AcademicYearFactory(
            year=a_year,
            start_date=datetime.datetime(a_year, now.month, 1),
            end_date=datetime.datetime(a_year + 1, now.month, 28)
        )
        self.education_group_year = EducationGroupYearFactory(education_group=self.education_group)

    def test_find_by_education_groups(self):
        self.assertCountEqual(education_group_year.find_by_education_groups([self.education_group]),
                              [self.education_group_year])
