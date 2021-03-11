import os, sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import unittest, time
from reportTemplate.HTMLTestRunnerCN import HTMLTestRunner

# 测试报告存放文件夹，如不存在，则自动创建一个report目录
if not os.path.exists(setting.TEST_REPORT):
    os.makedirs(setting.TEST_REPORT + '/' + "screenshot")

def add_case(test_path = setting.TEST_DIR):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*_test.py')
    return discover

def run_case(all_case, result_path = setting.TEST_REPORT):
    """执行所有的测试用例"""
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path + '/' + now + ' 测试报告.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='EMG系统自动化测试报告',
                            description='环境：windows 10 浏览器：chrome',
                            tester='Niko',
                            verbosity=2)
    runner.run(all_case)
    fp.close()


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
