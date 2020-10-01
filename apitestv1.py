import requests
import json
from time import mktime
from datetime import datetime


'''def post_data_check():
    
    url = "https://gorest.co.in/public-api/users"

    payload = { 'id': '1241253153155',
            'name' : 'Ashish',
            'status' : 'Active',
            'gender' : 'Male',
            'email' : 'ashissdfh@fil.com'}
    
    headers = {
    'Authorization': 'Bearer b3ca72d35e3f36cd25260afcd3be1e8f2b56dd1633722cc627b91e791a33d553'
    }
    
    files = {
        
    }

    response = requests.request("POST", url, headers=headers, data = payload, files = files)
    response_dict = json.loads(response.text.encode('utf8'))
    print(response_dict)

    if response_dict['code'] == 201:
        print("PASS -> Details added")
    else:
        print('FAIL')'''

def get_data_check():
    
    idpass = 5
    
    url = "https://gorest.co.in/public-api/users/{}".format(idpass)

    payload = { }
    headers = {
    'Authorization': 'Bearer b3ca72d35e3f36cd25260afcd3be1e8f2b56dd1633722cc627b91e791a33d553'
    }
    files = {}

    response = requests.request("GET", url, headers=headers, data = payload, files = files)
    response_dict = json.loads(response.text.encode('utf8'))
    print(response_dict)

    if response_dict['code'] == 200:
        print("PASS -> Details shown")
    else:
        print('FAIL')

#function calls

'''post_data_check()
'''
get_data_check()