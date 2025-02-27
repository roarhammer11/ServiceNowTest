import requests
from requests.auth import HTTPBasicAuth

class RequestUtility:
    def __init__(self, instanceUrl):
        self.url = f"https://{instanceUrl}/api/now/table/"
        
    def auth(self, username, password):
        return HTTPBasicAuth(username=username, password=password)

    def getRequest(self, urlEndpoint, auth, headers):
        return requests.get(self.url + urlEndpoint, auth=auth, headers=headers)
    
    def postRequest(self, urlEndpoint, auth, headers, payload):
        return requests.post(self.url + urlEndpoint, auth=auth, headers=headers, json=payload)