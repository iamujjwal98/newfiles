import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

url = "https://api.openbankproject.com/obp/v4.0.0/banks/aktivbank-pforzheim/atms/ATM_ID"

payload = {}
headers = {
  'Cookie': 'JSESSIONID=17ky6dyrblbuxsj81csdyr3wz'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))


#tests


def response_time():

    if response.elapsed:
        print("PASS, time elapsed: ",response.elapsed)
    else:
        print("FAIL")

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
        print("FAIL with version mismatch or param not found")
        
def cookie_check():
    
    if (response.cookies):
        print("PASS")
    else:
        print("FAIL")

def auth_check():
    response = requests.get('https://api.openbankproject.com', 
            auth = HTTPBasicAuth('ash101', 'HelloWorld1!'))
    print("Login",response)


#function calls
test_status_code_equals_200()
response_time()
response_type()
header_check()
content_body()
cookie_check()
auth_check()