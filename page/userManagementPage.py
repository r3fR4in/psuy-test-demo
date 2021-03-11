from page.basePage import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

"""用户管理"""
class userManagementPage(Page):

    # 搜索输入框
    queryByName_in = (By.XPATH, '/html/body/div[1]/div/div[2]/div/section/div/div[1]/label/div/div/div[2]/input')
    # 查询
    search_btn = (By.XPATH, '//*[@id="q-app"]/div/div[2]/div/section/div/div[1]/button[3]')
    # 新增
    add_btn = (By.XPATH, '//*[@id="q-app"]/div/div[2]/div/section/div/div[1]/button[2]/div[2]')
    # 登入名称
    loginName_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[1]/div[2]/div[1]/div[1]/input')
    # 用户名称
    userName_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[2]/div[2]/div[1]/div[1]/input')
    # 联络人
    contactPerson_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[3]/div[2]/div[1]/div[1]/input')
    # 电邮地址
    email_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[4]/div[2]/div[1]/div[1]/input')
    # 再次确认电邮地址
    checkEmail_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[5]/div[2]/div[1]/div[1]/input')
    # 新增服务号码
    addServiceNumber_btn = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[7]/div[2]/div/div/div/button')
    # 服务号码
    serviceNumber_div = (By.XPATH, '/html/body/div[5]/div[2]/div/div[1]/form/label[1]/div[2]')
    # 服务号码下拉选项第一项
    serviceNumber_div_1 = (By.XPATH, '/html/body/div[6]/div[2]/div')
    # 服务号码保存按钮
    serviceNumberSave_btn = (By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/button[2]')
    # 用户组别
    userGroup_div = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[8]/div[2]')
    # 用户保存按钮
    userSave_btn = (By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/button[2]')
    # 编辑
    edit_div = (By.XPATH, '//*[@id="q-app"]/div/div[2]/div/section/div/div[2]/table/tbody/tr/td[8]/button[1]')
    # 编辑的电邮地址
    edit_email_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[5]/div[2]/div[1]/div/input')
    # 编辑的再次确认电邮地址
    edit_checkEmail_in = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[6]/div[2]/div[1]/div/input')
    # 编辑框用户组别的span
    userGroup_span = (By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/form/label[10]/div[2]/div[1]/div[1]/div/span')


    def queryByName(self, val):
        self.input(val, *self.queryByName_in)
        self.click(*self.search_btn)

    def choose_userGroup_div(self, val):
        self.click(*self.userGroup_div)
        eles = self.find_elements(*(By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div'))
        i = 1  # 计数
        for ele in eles:
            if ele.get_attribute('innerHTML') == val:
                self.find_element(*(By.XPATH, "/html/body/div[5]/div[2]/div[" + str(i) + "]")).click()
                break
            i = i + 1
