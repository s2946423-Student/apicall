import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

username = input('Please enter your username: ')
password = getpass('Please enter your password: ')

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

token = response.json()['Token']

#    
    
#call another API

input("\nPress enter make an api request to get device count\n")

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/count"

payload={}
headers = {
  'X-Auth-Token': token,
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)








#Call a follow on request



