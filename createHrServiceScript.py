import requests
from requests.auth import HTTPBasicAuth

instance = "dev197684.service-now.com"
tableName = "sn_hr_core_service"
url = f"https://{instance}/api/now/table/{tableName}"
username = "test"
password = "Ash151515!"
payload = {"name":"Jenno","value":"test","badge":"6439a617c3b00300b599b4ad81d3ae57","fulfillment_type":"flow","flow":"30f3d26187e92300e0ef0cf888cb0b91","topic_detail":"24f0bd459f321200d9011977677fcfdf","producer":"396750d7c36fd61008adfb377d013105","case_options":"69cf86cf53922200d901a7e6a11c0827,c2d25d092f232200a9e7a310c18c954c","header_config_opened_for":"86d9872eb3900300f5302ddc16a8dc8b","header_config_subject_person":"c4e9872eb3900300f5302ddc16a8dc91"}
response = requests.post(url, auth=HTTPBasicAuth(username, password), headers={"Accept": "application/json"}, json=payload)
print(response)

#NOTE 1 Record producer should only have 1 HR Service
