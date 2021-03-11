import re

from page.userManagementPage import userManagementPage
from selenium.webdriver.common.by import By
from time import sleep


"""用户管理"""
class userManagementService(userManagementPage):

    """新增用户"""
    def addUser(self, datadict1, datadict2):
        self.click_userManagement_li()
        sleep(0.5)
        self.click(*self.add_btn)
        sleep(0.5)
        # 根据测试数据文件的字段数据判断，unique则输入uniqueData.yaml的数据，same则输入uniqueData.yaml的数据-1
        if datadict1['data']['loginName'] == 'unique':
            self.input(datadict2['loginName'], *self.loginName_in)
        elif datadict1['data']['loginName'] == 'same':
            number = re.sub('\D', '', datadict2['loginName'])
            list = datadict2['loginName'].split(number)
            self.input(list[0] + str(int(number) - 1), *self.loginName_in)
        else:
            self.input(datadict1['data']['loginName'], *self.loginName_in)

        if datadict1['data']['userName'] == 'unique':
            self.input(datadict2['loginName'], *self.userName_in)
        elif datadict1['data']['userName'] == 'same':
            number = re.sub('\D', '', datadict2['loginName'])
            list = datadict2['loginName'].split(number)
            self.input(list[0] + str(int(number) - 1), *self.userName_in)
        else:
            self.input(datadict1['data']['userName'], *self.userName_in)

        self.input(datadict1['data']['contactPerson'], *self.contactPerson_in)
        self.input(datadict1['data']['email'], *self.email_in)
        self.input(datadict1['data']['checkEmail'], *self.checkEmail_in)

        # 判断是否需要选择用户组别，为空则不选
        if datadict1['data']['userGroup'] != "":
            self.choose_userGroup_div(datadict1['data']['userGroup'])

        if datadict1['data']['serviceNumber'] != "":
            self.click(*self.addServiceNumber_btn)
            self.click(*self.serviceNumber_div)
            self.click(*self.serviceNumber_div_1)
            self.click(*self.serviceNumberSave_btn)

        sleep(0.8)
        self.click(*self.userSave_btn)
        actual = eval(datadict1['assert']['actual'])

        return actual
