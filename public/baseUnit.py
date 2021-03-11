from time import sleep
from selenium import webdriver
import unittest, yaml
from config import setting
from public.log import Log
import warnings
from service.loginService import loginService

log = Log()

class BaseTest(unittest.TestCase):
    """
    自定义BaseTest类
    """

    USERNAME = setting.USERNAME
    PASSWORD = setting.PASSWORD

    @classmethod
    def setUp(cls):
        # 忽略告警信息
        warnings.simplefilter('ignore', ResourceWarning)

        try:
            f = open(setting.TEST_DATA_YAML + '/' + 'uniqueData.yaml', encoding='utf-8')
            cls.uniqueData = yaml.load(f, Loader=yaml.FullLoader)
        except FileNotFoundError as file:
            log.error("文件不存在：{0}".format(file))

        """
        由于HTMLTestRunner报告在出错时会调用截图函数，如果在tearDown里关闭浏览器会导致找不到浏览器而截图报错，
        所以在setup先尝试关闭一次浏览器，最后再在tearDownClass做最后一次关闭浏览器操作
        """
        try:
            cls.driver.quit()
        except:
            pass

        cls.driver = cls.initDriver(webdriver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def initDriver(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
        # driver.set_window_size(1920, 1080)

        return driver

    def login(self, driver, username=USERNAME, password=PASSWORD):
        # 登录
        loginService(driver).login(username, password)


