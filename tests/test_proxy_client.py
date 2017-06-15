# -*- coding: utf-8 -*-
import pytest
from mock import MagicMock
from requests.models import Response, HTTPError

from proxy_bonanza.client import ProxyBonanzaClient


@pytest.fixture
def response_content():
    return '{"success":true,"data":{"id":48788,"login":"fakelogin","password":"qwerty123","expires":"2017-10-31T00:00:00+0000","bandwidth":1492664315943,"last_ip_change":"2016-08-23T00:00:00+0000","ippacks":[{"id":19316,"ip":"123.45.678.910","port_http":60099,"port_socks":61336,"active":true,"modified":"2016-05-22T06:44:24+0000","proxyserver":{"georegion_id":13,"georegion":{"name":"Sao Paulo","country":{"id":15,"isocode":"BR","name":"Brazil","flag_image":"br.gif","continent":"southamerica","eunion":false,"vat_rate":null}}}},{"id":19396,"ip":"321.45.876.999","port_http":60099,"port_socks":61336,"active":true,"modified":"2016-05-22T06:44:24+0000","proxyserver":{"georegion_id":13,"georegion":{"name":"Sao Paulo","country":{"id":15,"isocode":"BR","name":"Brazil","flag_image":"br.gif","continent":"southamerica","eunion":false,"vat_rate":null}}}}],"authips":[],"package":{"parent_id":null,"name":"International","bandwidth":10737418240,"price":36,"howmany_ips":10,"price_per_gig":1.5,"package_type":"geo","created":null,"modified":null}}}'


@pytest.fixture
def get_data_from_userpackage_id():
    return {u'authips': [],
            u'bandwidth': 1492664315943,
            u'expires': u'2017-10-31T00:00:00+0000',
            u'id': 48788,
            u'ippacks': [{u'active': True,
                          u'id': 19316,
                          u'ip': u'123.45.678.910',
                          u'modified': u'2016-05-22T06:44:24+0000',
                          u'port_http': 60099,
                          u'port_socks': 61336,
                          u'proxyserver': {u'georegion': {u'country': {u'continent': u'southamerica',
                                                                       u'eunion': False,
                                                                       u'flag_image': u'br.gif',
                                                                       u'id': 15,
                                                                       u'isocode': u'BR',
                                                                       u'name': u'Brazil',
                                                                       u'vat_rate': None},
                                                          u'name': u'Sao Paulo'},
                                           u'georegion_id': 13}},
                         {u'active': True,
                          u'id': 19396,
                          u'ip': u'321.45.876.999',
                          u'modified': u'2016-05-22T06:44:24+0000',
                          u'port_http': 60099,
                          u'port_socks': 61336,
                          u'proxyserver': {u'georegion': {u'country': {u'continent': u'southamerica',
                                                                       u'eunion': False,
                                                                       u'flag_image': u'br.gif',
                                                                       u'id': 15,
                                                                       u'isocode': u'BR',
                                                                       u'name': u'Brazil',
                                                                       u'vat_rate': None},
                                                          u'name': u'Sao Paulo'},
                                           u'georegion_id': 13}}],
            u'last_ip_change': u'2016-08-23T00:00:00+0000',
            u'login': u'fakelogin',
            u'package': {u'bandwidth': 10737418240,
                         u'created': None,
                         u'howmany_ips': 10,
                         u'modified': None,
                         u'name': u'International',
                         u'package_type': u'geo',
                         u'parent_id': None,
                         u'price': 36,
                         u'price_per_gig': 1.5},
            u'password': u'qwerty123'
            }


@pytest.fixture
def get_data_from_api():
    return [{'bandwidth': 34192444911,
             'expires': '2015-02-06T00:00:00+0000',
             'id': 212121,
             'last_ip_change': '2014-11-10T00:00:00+0000',
             'login': 'fakelogin',
             'package': {'bandwidth': 10737418240,
                         'howmany_ips': 1,
                         'name': 'Special 3',
                         'package_type': 'exclusive',
                         'price': 5,
                         'price_per_gig': 1},
             'password': 'qwerty123'},
            {'bandwidth': 3433019582,
             'expires': '2015-01-01T00:00:00+0000',
             'id': 31313131,
             'last_ip_change': '2014-07-28T00:00:00+0000',
             'login': 'fakelogin',
             'package': {'bandwidth': 2147483648,
                         'howmany_ips': 2,
                         'name': 'International',
                         'package_type': 'geo',
                         'price': 12,
                         'price_per_gig': 2},
             'password': 'fakelogin'}]


def test_error_when_api_key_is_not_provided():
    with pytest.raises(RuntimeError):
        ProxyBonanzaClient()


def test_getting_user_package_ids(monkeypatch, get_data_from_api):
    monkeypatch.setattr("proxy_bonanza.client.ProxyBonanzaClient._get_api_data", MagicMock(return_value=get_data_from_api))
    client = ProxyBonanzaClient(api_key='fake123api')

    ids = client.get_user_package_ids()
    assert ids == [212121, 31313131]


def test_getting_user_packages(monkeypatch, get_data_from_api):
    monkeypatch.setattr("proxy_bonanza.client.ProxyBonanzaClient._get_api_data", MagicMock(return_value=get_data_from_api))
    client = ProxyBonanzaClient(api_key='fake123api')

    packages = client.get_user_packages()
    assert packages == get_data_from_api


def test_getting_proxies(monkeypatch, get_data_from_userpackage_id):
    monkeypatch.setattr("proxy_bonanza.client.ProxyBonanzaClient._get_api_data", MagicMock(return_value=get_data_from_userpackage_id))
    client = ProxyBonanzaClient(api_key='fake123api')

    proxies = client.get_proxies(212121)
    assert proxies == [{u'active': True,
                        u'id': 19316,
                        u'ip': u'123.45.678.910',
                        u'modified': u'2016-05-22T06:44:24+0000',
                        u'port_http': 60099,
                        u'port_socks': 61336,
                        u'proxyserver': {u'georegion': {u'country': {u'continent': u'southamerica',
                                                                     u'eunion': False,
                                                                     u'flag_image': u'br.gif',
                                                                     u'id': 15,
                                                                     u'isocode': u'BR',
                                                                     u'name': u'Brazil',
                                                                     u'vat_rate': None},
                                                        u'name': u'Sao Paulo'},
                                         u'georegion_id': 13},
                        u'login': u'fakelogin',
                        u'password': u'qwerty123'},
                       {u'active': True,
                        u'id': 19396,
                        u'ip': u'321.45.876.999',
                        u'modified': u'2016-05-22T06:44:24+0000',
                        u'port_http': 60099,
                        u'port_socks': 61336,
                        u'proxyserver': {u'georegion': {u'country': {u'continent': u'southamerica',
                                                                     u'eunion': False,
                                                                     u'flag_image': u'br.gif',
                                                                     u'id': 15,
                                                                     u'isocode': u'BR',
                                                                     u'name': u'Brazil',
                                                                     u'vat_rate': None},
                                                        u'name': u'Sao Paulo'},
                                         u'georegion_id': 13},
                        u'login': u'fakelogin',
                        u'password': u'qwerty123'}]


def test_getting_data_with_bad_response(monkeypatch):
    response = Response()
    response.status_code = 401

    monkeypatch.setattr("requests.get", MagicMock(return_value=response))

    client = ProxyBonanzaClient(api_key='fake123api')
    with pytest.raises(HTTPError):
        client._get_api_data('www.abc.com.br')


def test_getting_data_with_successful_response(monkeypatch, response_content):
    response = Response()
    response.status_code = 202
    response._content = response_content

    monkeypatch.setattr("requests.get", MagicMock(return_value=response))

    client = ProxyBonanzaClient(api_key='fake123api')
    data = client._get_api_data('www.abc.com.br')
    assert data == {u'authips': [],
                    u'bandwidth': 1492664315943,
                    u'expires': u'2017-10-31T00:00:00+0000',
                    u'id': 48788,
                    u'ippacks': [{u'active': True,
                                  u'id': 19316,
                                  u'ip': u'123.45.678.910',
                                  u'modified': u'2016-05-22T06:44:24+0000',
                                  u'port_http': 60099,
                                  u'port_socks': 61336,
                                  u'proxyserver': {u'georegion': {u'country': {u'continent': u'southamerica',
                                                                               u'eunion': False,
                                                                               u'flag_image': u'br.gif',
                                                                               u'id': 15,
                                                                               u'isocode': u'BR',
                                                                               u'name': u'Brazil',
                                                                               u'vat_rate': None},
                                                                  u'name': u'Sao Paulo'},
                                                   u'georegion_id': 13}},
                                 {u'active': True,
                                  u'id': 19396,
                                  u'ip': u'321.45.876.999',
                                  u'modified': u'2016-05-22T06:44:24+0000',
                                  u'port_http': 60099,
                                  u'port_socks': 61336,
                                  u'proxyserver': {u'georegion': {u'country': {u'continent': u'southamerica',
                                                                               u'eunion': False,
                                                                               u'flag_image': u'br.gif',
                                                                               u'id': 15,
                                                                               u'isocode': u'BR',
                                                                               u'name': u'Brazil',
                                                                               u'vat_rate': None},
                                                                  u'name': u'Sao Paulo'},
                                                   u'georegion_id': 13}}],
                    u'last_ip_change': u'2016-08-23T00:00:00+0000',
                    u'login': u'fakelogin',
                    u'package': {u'bandwidth': 10737418240,
                                 u'created': None,
                                 u'howmany_ips': 10,
                                 u'modified': None,
                                 u'name': u'International',
                                 u'package_type': u'geo',
                                 u'parent_id': None,
                                 u'price': 36,
                                 u'price_per_gig': 1.5},
                    u'password': u'qwerty123'}
