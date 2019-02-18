import json

import requests
from dal import autocomplete
from django import http
from django.conf import settings


class CountryAutocomplete(autocomplete.Select2ListView):

    def get(self, request, *args, **kwargs):
        return http.HttpResponse(json.dumps({
            'results': [
                {'id': country['uuid'], 'text': country['name']}
                for country in self.get_country_list_from_osis(name_filter=self.q)
            ]
        }), content_type='application/json')

    def get_country_list_from_osis(self, name_filter=None):
        header_to_get = {'Authorization': 'Token ' + settings.OSIS_PORTAL_TOKEN}
        url = settings.URL_COUNTRY_API

        response = requests.get(
            url=url,
            headers=header_to_get,
            data={'search': name_filter or ""}
        )

        data = response.json()
        if 'results' in data:
            data = data['results']
        return data
