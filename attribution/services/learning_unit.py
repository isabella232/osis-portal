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
from typing import List

import osis_learning_unit_sdk
import urllib3
from django.conf import settings
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.effective_class import EffectiveClass

from base.models.person import Person
from frontoffice.settings.osis_sdk import learning_unit as learning_unit_sdk

logger = logging.getLogger(settings.DEFAULT_LOGGER)


class LearningUnitService:
    @staticmethod
    def get_learning_unit_title(year: int, acronym: str, person: Person) -> List:
        configuration = learning_unit_sdk.build_configuration(person)
        with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
            api_instance = learning_units_api.LearningUnitsApi(api_client)
            try:
                learning_unit_title = api_instance.learningunitstitle_read(year=year, acronym=acronym)['title']
            except (osis_learning_unit_sdk.ApiException, urllib3.exceptions.HTTPError,) as e:
                # Run in degraded mode in order to prevent crash all app
                logger.error(e)
                learning_unit_title = ''
        return learning_unit_title

    @staticmethod
    def get_effective_classes(year: int, acronym: str, person: Person) -> List[EffectiveClass]:
        configuration = learning_unit_sdk.build_configuration(person)
        with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
            api_instance = learning_units_api.LearningUnitsApi(api_client)
            try:
                effective_classes = api_instance.get_learning_unit_classes(year=year, acronym=acronym)
            except (osis_learning_unit_sdk.ApiException, urllib3.exceptions.HTTPError,) as e:
                # Run in degraded mode in order to prevent crash all app
                logger.error(e)
                effective_classes = []
        return effective_classes
