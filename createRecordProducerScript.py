import requests
from requests.auth import HTTPBasicAuth

instance = "dev197684.service-now.com"
tableName = "sc_cat_item_producer"
url = f"https://{instance}/api/now/table/{tableName}"
username = "test"
password = "Ash151515!"
applicationScopeScript = "new sn_hr_core.hr_ServicesUtil(current, gs).createCaseFromProducer(producer, cat_item.sys_id);"
payload = {"name":"x", "active":"true","table_name":"sn_hr_core_case","owner":"","script":applicationScopeScript,"sc_catalogs":"e0d08b13c3330100c8b837659bba8fb4","no_save_as_draft":"true","no_attachment_v2":"true"}
response = requests.post(url, auth=HTTPBasicAuth(username, password), headers={"Accept": "application/json"}, json=payload)
print(response)
print(response.headers["Location"].replace(url + "/",""))