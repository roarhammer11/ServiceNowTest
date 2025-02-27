import requests
from requests.auth import HTTPBasicAuth

instance = "dev197684.service-now.com"
url = f"https://{instance}/api/now/table/sys_user"
username = "test"
password = "Ash151515!"
print(url)
response = requests.get(url, auth=HTTPBasicAuth(username, password), headers={"Accept": "application/json"})

print(response.json())