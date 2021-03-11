import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# url
URL = "http://172.30.22.124:8001/login"
# 用户名
USERNAME = "school_admin"
# 密码
PASSWORD = "Aa123456"
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR, "testcase")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "logs")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR, "testdata")
# 测试附件
TEST_FILE_DIR = os.path.join(BASE_DIR, "testfile")
# 元素控件
# TEST_Element_YAML = os.path.join(BASE_DIR, "testyaml")
