from requestUtility import RequestUtility

projectMasterList = ["HRWF"]

class HRWF:
    def __init__(self, instanceUrl, username, password):
        self.__rq = RequestUtility(instanceUrl)
        self.__username = username
        self.__password = password
    
    def createApplication(self, applicationScope):
        ...

    def __createRecordProducer(self, applicationScope):
        if(applicationScope == "hrwf"):
            applicationScopeScript = "new sn_hr_core.hr_ServicesUtilV2(current, gs).createCaseFromProducer(producer, cat_item.sys_id);"
        else:
            applicationScopeScript = "new sn_hr_core.hr_ServicesUtil(current, gs).createCaseFromProducer(producer, cat_item.sys_id);\nnew x_ict2_snxhr_wp.CaseResubmissionActionUse().updateCaseByResubmission(current, producer);"
        payload = {"name":"x", "active":"true","table_name":"sn_hr_core_case","owner":"","script":applicationScopeScript,"sc_catalogs":"e0d08b13c3330100c8b837659bba8fb4","no_save_as_draft":"true","no_attachment_v2":"true"}
        self.__createRecord("sc_cat_item_producer", payload)
        ...

    def __createHrCase(self):
        ...
    
    def __createRecord(self, urlEndpoint, payload):
        return self.__rq.postRequest(urlEndpoint, self.__rq.auth(self.__username, self.__password), {"Accept": "application/json"}, payload)
    