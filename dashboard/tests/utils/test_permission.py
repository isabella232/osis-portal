##############################################################################
#
# OSIS stands for Open Student Information System. It's an application
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
from dashboard.utils import permission
from base.tests.models import test_academic_year, test_academic_calendar

now = datetime.datetime.now()
CURRENT_YEAR = now.year
NEXT_YEAR = now.year + 1


class TestPermission(TestCase):

    def test_permission_is_undefined_no_academic_year(self):
        self.assertEqual(permission.is_online_application_opened(), False)

    def test_permission_is_undefined_no_academic_calendar(self):
        test_academic_year.create_academic_year_with_year(CURRENT_YEAR)
        test_academic_year.create_academic_year_with_year(NEXT_YEAR)
        self.assertEqual(permission.is_online_application_opened(), False)

    def test_permission_is_undefined(self):
        test_academic_year.create_academic_year_with_year(CURRENT_YEAR)
        next_academic_year = test_academic_year.create_academic_year_with_year(NEXT_YEAR)
        test_academic_calendar.create_academic_calendar(next_academic_year, permission.APPLICATION_SESSION_TITLE,
                                                        datetime.datetime(now.year, now.month, 1),
                                                        datetime.datetime(now.year, now.month+2, 1))
        self.assertEqual(permission.is_online_application_opened(), True)
