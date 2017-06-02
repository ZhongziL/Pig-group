#-*- coding:utf-8 -*-

import httplib
import urllib
from flask import current_app
from threading import Thread

host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#->APIID
account  = "C70913215" 
#->APIKEY
password = "125ff924fc601a4dcc88a29cdb5c6ae2"

def send_sms(app, text, mobile):
    with app.app_context():
        content = "您的验证码是："+ text +"。请不要把验证码泄露给其他人。"
        params = urllib.urlencode({'account': account, 'password' : password, 'content': content, 'mobile':mobile,'format':'json' })
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPConnection(host, port=80, timeout=60)
        conn.request("POST", sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        print(response_str)
        return response_str

def send_out(text, mobile):
    app = current_app._get_current_object()
    thr = Thread(target=send_sms, args=[app, text, mobile])
    thr.start()
    return thr

