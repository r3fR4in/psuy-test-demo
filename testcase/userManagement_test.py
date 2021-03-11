from time import sleep

from public import baseUnit
import yaml, unittest
from config import setting
from public.log import Log
from service.userManagementService import userManagementService
from service.loginService import loginService
from public import GetYaml
from selenium.webdriver.common.by import By
from public import my_ddt


log = Log()
try:
    f = open(setting.TEST_DATA_YAML + '/' + 'addUserData.yaml', encoding='utf-8')
    addUserData = yaml.load(f, Loader=yaml.FullLoader)
except FileNotFoundError as file:
    log.error("文件不存在：{0}".format(file))

@my_ddt.ddt
class userManagement_test(baseUnit.BaseTest):
    """用户管理"""

    @my_ddt.data(*addUserData)
    def test_01_addUser(self, datayaml):
        """={0}"""
        self.login(self.driver)
        service = userManagementService(self.driver)
        actual = service.addUser(datayaml, self.uniqueData[0])
        self.assertIn(datayaml['assert']['expected'], actual)
        if datayaml['assert']['isSuccess'] == "true":
            Yaml = GetYaml.getyaml(setting.TEST_DATA_YAML + '/' + 'uniqueData.yaml')
            Yaml.dataIncreasing("loginName")
            service.queryByName(self.uniqueData[0]['loginName'])
            sleep(1)
            service.click(*service.edit_div)
            self.assertIn(self.uniqueData[0]['loginName'], service.getValue(*service.loginName_in))
            self.assertIn(self.uniqueData[0]['loginName'], service.getValue(*service.userName_in))
            self.assertIn(datayaml['data']['contactPerson'], service.getValue(*service.contactPerson_in))
            self.assertIn(datayaml['data']['email'], service.getValue(*service.edit_email_in))
            self.assertIn(datayaml['data']['checkEmail'], service.getValue(*service.edit_checkEmail_in))
            self.assertIn(datayaml['data']['userGroup'], service.getinnerHTML(*service.userGroup_span))



if __name__ == '__main__':
    unittest.main()

