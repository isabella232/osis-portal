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
import json
import datetime
from django.conf import settings
from frontoffice.queue.queue_listener import AttestationClient


def fetch_json_attestation(registration_id, attestation_type):
    json_attestation = None
    message = generate_fetch_message(registration_id, attestation_type)
    if message:
        client = AttestationClient()
        json_data = client.call(message)
        if json_data:
            json_attestation = json.loads(json_data.decode("utf-8"))
    return json_attestation


def generate_fetch_message(registration_id, attestation_type):
    if registration_id:
        return json.dumps({'registration_id': registration_id,
                           'attestation_type': attestation_type})
    return None
