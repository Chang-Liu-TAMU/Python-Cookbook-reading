# @Time: 2022/4/29 14:56
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:11.1.Interacting_with_HTTP_services_as_a_client.py

#part1
from urllib import request, parse

#make a GET request
# url = "http://httpbin.org/get"
#
# parms = {
#     "name1": "value1",
#     "name2": "value2"
# }
#
# querystring = parse.urlencode(parms)

# u = request.urlopen(url + "?" + querystring)
# resp = u.read()
# print(resp)

#make a POST request
# url = "http://httpbin.org/post"
# parms = {
#     "name1": "value1",
#     "name2": "value2"
# }
#
# querystring = parse.urlencode(parms)
# u = request.urlopen(url, querystring.encode("ascii"))
# resp = u.read()
# print(resp)


#supply some custom http headers
# url = "some_url"
#
# headers = {
#     "User-agent": "none/ofyourbusiness",
#     "Spam": "Eggs"
# }
#
# querystring = "some_query_string"
#
# req = request.Request(url, querystring.encode("ascii"), headers=headers)
#
# u = request.urlopen(req)
# resp = u.read()



#using request

import requests

# url = "http://httpbin.org/post"
# parms = {
#     "name1": "value1",
#     "name2": "value2"
# }
#
# headers = {
#     "User-agent": "some idiot headers",
#     "Spam": "eggs"
# }
#
# resp = requests.post(url, data=parms, headers=headers)
#
# text = resp.text
# print(text)



#make a HEAD request
# import requests
# resp = requests.head('http://www.python.org/index.html')
# status = resp.status_code
# last_modified = resp.headers['last-modified']
# content_type = resp.headers['content-type']
# content_length = resp.headers['content-length']
# print(last_modified)
# print(content_length)
# print(content_length)


# import requests
# resp = requests.get('http://pypi.python.org/pypi?:action=login',
#  auth=('user','password'))


# #passing cookies
# import requests
# # First request
# resp1 = requests.get("some_url1")
# resp2 = requests.get("some_url2", cookies=resp1.cookies)
#
# #upload content
# url = 'http://httpbin.org/post'
# files = { 'file': ('data.csv', open('data.csv', 'rb')) }
# r = requests.post(url, files=files)


#stick entirely with built-in urllib
# from http.client import HTTPConnection
# from urllib import parse
# c = HTTPConnection('www.python.org', 80)
# c.request('HEAD', '/index.html')
# resp = c.getresponse()
# print('Status', resp.status)
# for name, value in resp.getheaders():
#     print(name, value)


# For example, here is a sample of code that
# authenticates to the Python package index
#awkward and verbose
# import urllib.request
# import urllib
# auth = urllib.request.HTTPBasicAuthHandler()
# auth.add_password('pypi','http://pypi.python.org','username','password')
# opener = urllib.request.build_opener(auth)
# r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
# u = opener.open(r)
# resp = u.read()


#Working with a site such as httpbin.org is often preferable
# to experimenting with a real site
import requests
r = requests.get('http://httpbin.org/get?name=Dave&n=37',
                 headers = { 'User-agent': 'goaway/1.0' })
resp = r.json()
print(resp["headers"])
print(resp["args"])