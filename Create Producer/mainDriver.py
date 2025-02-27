import os
from GUI import GUI
from requestUtility import RequestUtility
from dotenv import load_dotenv

load_dotenv()

instanceUrl = os.getenv("INSTANCE_URL")
username = os.getenv("INSTANACE_USERNAME")
password = os.getenv("INSTANCE_PASSWORD")
gui = GUI(instanceUrl, username, password)

# urlEndpoint = "/sys_user"
gui.exec()
# print(rq.getRequest(urlEndpoint, rq.auth(username, password), headers={"Accept": "application/json"}).json())