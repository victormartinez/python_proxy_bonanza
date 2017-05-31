# python-proxy-bonanza

A lightweight client to get proxies from Proxy Bonanza service


## Usage

At first it is necessary to get the user package ids and, then, get the proxies available for each id.

```
from proxy_bonanza.client import ProxyBonanzaClient

client = ProxyBonanzaClient(api_key='<YOUR_API_KEY>')
ids = client.get_user_package_ids()
proxies = client.get_proxies(<YOUR_ID>)

```

### Obtaining User Package ids

```
> client.get_user_package_ids()

[5478, 9870, 1209]
```

### Obtaining Proxies


```
> client.get_proxies(id1)

{
    u'active': True,
    u'id': 19316,
    u'ip': u'123.45.678.910',
    u'modified': u'2016-05-22T06:44:24+0000',
    u'port_http': 60099,
    u'port_socks': 61336,
    u'proxyserver': {
        u'georegion': {
            u'country': {
                u'continent': u'southamerica',
                u'eunion': False,
                u'flag_image': u'br.gif',
                u'id': 15,
                u'isocode': u'BR',
                u'name': u'Brazil',
                u'vat_rate': None
            },
        u'name': u'Sao Paulo'
        },
        u'georegion_id': 13
    },
    u'login': u'fakelogin',
    u'password': u'qwerty123'
}
```

### Contributing
1. Clone the repository
1. Create a virtualenv and install the requirements.txt
1. Develop the feature or fix
1. Create and execute the tests using pytest
1. Open a Pull Request =)

