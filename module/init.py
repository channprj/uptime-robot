# test.py
import __future__
import sys
import httplib
import urllib

class HTTPChecker(object):
    """docstring for HTTPChecker"""
    def __init__(self, arg):
        super(HTTPChecker, self).__init__()
        self.arg = arg

def test_print():
    # res = sys.version
    print("        NOW THIS PROJECT IS WORKING IN PROGRESS...")
    res = send_http_request('google.com')
    return str(res)

def send_http_request(url):
    print("        send_http_request()...")
    conn = httplib.HTTPConnection(url)
    conn.request('HEAD', '')
    res = conn.getresponse()
    status = res.status
    return status

def send_ping_request():
    pass

def alert_email():
    pass

def alert_sms():
    pass

def __init__(self):
    return
