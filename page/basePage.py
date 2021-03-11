import os,sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.common.exceptions import NoSuchFrameException,NoSuchWindowException,NoAlertPresentException
import configparser
from public.log import Log


# 读取配置文件的URL
login_url = setting.URL
log = Log()

class Page(object):
    """
    基础类，用于页面对象类的继承
    """
    def __init__(self, selenium_driver, base_url=login_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.parent = parent
        self.timeout = 10

    # 帐户
    account_div = (By.XPATH, '//*[@id="q-app"]/div/div[1]/aside/div/div/div[1]/div/div/div[1]/div/div[1]')
    # 帐户-用户管理
    userManagement_li = (By.XPATH, '//*[@id="q-app"]/div/div[1]/aside/div/div/div[1]/div/div/div[1]/div/div[2]/ul/li[2]')


    def click_userManagement_li(self):
        self.find_element(*self.account_div).click()
        self.find_element(*self.userManagement_li).click()


    # def on_page(self):
    #     """
    #     URL地址断言
    #     :return: URL地址
    #     """
    #     return self.driver.current_url == (self.base_url + self.url)

    # def _open(self,url):
    #     """
    #     打开浏览器URL访问
    #     :param url: URL地址
    #     :return:
    #     """
    #     url = self.base_url + url
    #     self.driver.get(url)
    #     assert self.on_page(), 'Did not land on %s' % url
    #     print(self.url)

    def open(self):
        # """
        # 内部调用_open私有函数
        # :return:
        # """
        # self._open(self.url)
        url = self.base_url
        self.driver.get(url)

    def find_element(self, *loc):
        """
        单个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            log.error("{0}页面中未能找到{1}元素".format(self, loc))

    def find_elements(self, *loc):
        """
        多个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            log.error("{0}页面中未能找到{1}元素".format(self, loc))

    # def script(self, src):
    #     """
    #     提供调用JavaScript方法
    #     :param src: 脚本文件
    #     :return: JavaScript脚本
    #     """
    #     return self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_key(self, *loc, value, click_first=True, clear_first=True):
        try:
            # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            log.error("%s 页面中未能找到 %s 元素" % (self, loc))

    def switch_frame(self, loc):
        """
        多表单嵌套切换
        :param loc: 传元素的属性值
        :return: 定位到的元素
        """
        try:
            return self.driver.switch_to_frame(loc)
        except NoSuchFrameException as msg:
            log.error("查找iframe异常-> {0}".format(msg))

    def switch_windows(self, loc):
        """
        多窗口切换
        :param loc:
        :return:
        """
        try:
            return self.driver.switch_to.window(loc)
        except NoSuchWindowException as msg:
            log.error("查找窗口句柄handle异常-> {0}".format(msg))

    def switch_alert(self):
        """
        警告框处理
        :return:
        """
        try:
            return self.driver.switch_to_alert()
        except NoAlertPresentException as msg:
            log.error("查找alert弹出框异常-> {0}".format(msg))

    def click(self, *loc):
        """点击"""
        self.find_element(*loc).click()

    def input(self, val, *loc):
        """输入"""
        self.find_element(*loc).send_keys(Keys.CONTROL, "a")
        self.find_element(*loc).send_keys(Keys.BACK_SPACE)
        self.find_element(*loc).send_keys(val)

    def getValue(self, *loc):
        """获取输入框的值"""
        val = self.find_element(*loc).get_attribute('value')

        return val

    def getinnerHTML(self, *loc):
        """获取HTML的文本值"""
        val = self.find_element(*loc).get_attribute('innerHTML')

        return val
