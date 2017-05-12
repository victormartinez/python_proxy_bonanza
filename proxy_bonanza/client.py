# -*- coding: utf-8 -*-
import json

import requests


class ProxyBonanzaClient(object):
    USER_PACKAGES_ENDPOINT = "https://api.proxybonanza.com/v1/userpackages.json"
    PROXIES_URL_ENDPOINT_TEMPLATE = "https://api.proxybonanza.com/v1/userpackages/{}.json"

    def __init__(self, api_key=None):
        if api_key is None:
            raise RuntimeError("No API key provided.")
        self._api_key = api_key

    def get_proxies(self, user_package_id):
        '''
        Get the list of proxies available based on the user package id

        :param user_package_id:
        :return: list of dictionaries containing the keys active, id, ip,
                 modified, port_http, port_socks, proxyserver
        '''
        api_url = self.PROXIES_URL_ENDPOINT_TEMPLATE.format(user_package_id)
        data = self._get_api_data(api_url)
        return self._get_proxies_with_correspondent_auth(data)

    def _get_proxies_with_correspondent_auth(self, data):
        login = data['login']
        password = data['password']
        ip_packs = data['ippacks']

        [i.update({u'login': login, u'password': password}) for i in ip_packs]
        return ip_packs

    def get_user_package_ids(self):
        data_list = self._get_api_data(self.USER_PACKAGES_ENDPOINT)
        return [d['id'] for d in data_list]

    def get_user_packages(self):
        return self._get_api_data(self.USER_PACKAGES_ENDPOINT)

    def _get_api_data(self, api_url):
        '''
        Given an endpoint, it requests the API and return the value inside the 'data' key

        :param api_url: api endpoint
        :return: dictionary or list of dictionaries that resides in the data key
        '''
        response = requests.get(api_url, headers={'Authorization': self._api_key})
        if not response.ok:
            response.raise_for_status()

        content = response.content
        if isinstance(content, bytes):
            content = content.decode('utf-8')

        json_result = json.loads(content)
        return json_result['data']
