# init.py
import __future__
import sys
import httplib
import urllib
import re

class HTTPChecker(object):
    """docstring for HTTPChecker"""
    def __init__(self, arg):
        super(HTTPChecker, self).__init__()
        self.arg = arg

def test_print():
    res = send_http_request('chann.kr')
    return str(res)

def send_http_request(url):
    conn = httplib.HTTPConnection(url)
    conn.request('HEAD', '')
    res = conn.getresponse()
    status = res.status
    # status = res.getheaders()
    return status

def send_ping_request():
    pass

def alert_email():
    pass

def alert_sms():
    pass

def is_email_address_valid(email):
    """Validate email address using regular expression."""
    if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
        return False
    return True

def set_interval():
    pass

def __init__():
    return
