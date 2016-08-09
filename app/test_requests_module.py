from __future__ import unicode_literals

import requests


def http_request(event, context):
    options = {
        'domain': 'chann.kr',
        'protocol': 'https',
        'path': '/',
        'method': 'GET',
        'allow_redirects': False,
        'timeout': 5,
    }
    options.update(event)
    response = requests.request(options['method'], '{protocol}://{domain}{path}'.format(**options), allow_redirects=options['allow_redirects'], timeout=options['timeout'])
    response.raise_for_status()
    print(response)

print(http_request({'domain':'blog.chann.kr',},1))
