import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from time import mktime
from datetime import datetime

url = "https://api.openbankproject.com/obp/v4.0.0/root"

payload = {}
headers = {
  'Authorization': 'Basic YXNoMTAxOkhlbGxvd29ybGQxIQ==',
  'Cookie': 'JSESSIONID=17ky6dyrblbuxsj81csdyr3wz'
}

response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))
print(response.encoding)
sessionid = response.cookies.get('Cookie')

#unit tests

def response_time():

    if response.elapsed:
        print("PASS, time elapsed: ",response.elapsed)
    else:
        print("FAIL")

def api_uri_check():
    
    if url == "https://api.openbankproject.com/obp/v4.0.0/":
        print("PASS -> correct url")
    else:
        print("FAIL -> incorrect url")

def test_status_code_equals_200():
    
    if (response.status_code == 200):
        print("PASS")
    else:
        print("FAIL ,the status code is: ", response.status_code)

def response_type():

    #response = requests.get("https://api.openbankproject.com/obp/v4.0.0/root")
    if (response.json()):
        print("PASS")
    else:
        print("FAIL")

def header_check():

    if('Content-Type' in response.headers):
        print("PASS")
    else:
        print("FAIL")

def content_body():
    response_content = response.json()
    if("version" in response_content and response_content["version"] == "v4.0.0"):
        print("PASS with version:v4.0.0")
    else:
        print("FAIL with version mismatch")

def cookie_check():
    
    if (response.cookies):
        print("PASS")
    else:
        print("FAIL")

def encoding_check():
    resp = response.encoding
    if(resp == 'utf-8'):
        print("PASS")
    else:
        print("FAIL")

def auth_check():
    response = requests.get('https://api.openbankproject.com/obp/v4.0.0/root', 
            auth = HTTPBasicAuth('ash101', 'pass'))
    print(response)


#function calls
test_status_code_equals_200()
response_time()
api_uri_check()
response_type()
header_check()
content_body()
cookie_check()
encoding_check()
auth_check()