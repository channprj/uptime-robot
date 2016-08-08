# init.py
import __future__
import sys
import httplib
import urllib
import models

from flask import Flask

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
    return status, res.getheaders()

def send_ping_request():
    pass

def alert_email():
    pass

def alert_sms():
    pass

def set_interval():
    pass

def __init__():
    return
