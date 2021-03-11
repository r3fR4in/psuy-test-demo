import yaml
import re

class getyaml:
    def __init__(self,filepath):
        self.path = filepath

    def get_yaml(self):
        '''
        加载yaml文件数据
        :param path: 文件路径
        :return:返回数据
        '''
        try:
            f = open(self.path, encoding='utf-8')
            data =yaml.load(f)
            f.close()
            return data
        except Exception as msg:
            print("异常消息-> {0}".format(msg))

    def alldata(self):
        """
        读取yaml文件数据
        :return: 返回数据
        """
        data =self.get_yaml()
        return data

    def caselen(self):
        """
        testcase字典长度
        :return: 字典长度大小
        """
        data = self.alldata()
        length = len(data['testcase'])
        return length

    def checklen(self):
        """
        check字典长度
        :return: 字典长度大小
        """
        data = self.alldata()
        length = len(data['check'])
        return length

    def get_elementinfo(self, i):
        """
        获取testcase项的element_info元素
        :param i: 位置序列号
        :return: 返回element_info元素数据
        """
        data = self.alldata()
        return data['testcase'][i]['element_info']

    def get_find_type(self, i):
        """
        获取testcase项的find_type元素数据
        :param i: 位置序列号
        :return: 返回find_type元素数据
        """
        data = self.alldata()
        return data['testcase'][i]['find_type']

    def get_operate_type(self, i):
        """
        获取testcase项的operate_type元素数据
        :param i: 位置序列号
        :return: 返回operate_type元素数据
        """
        data = self.alldata()
        return data['testcase'][i]['operate_type']

    def get_CheckElementinfo(self, i):
        """
        获取check项的element_info元素
        :param i: 位置序列号
        :return: 返回element_info元素数据
        """
        data = self.alldata()
        return data['check'][i]['element_info']

    def get_CheckFindType(self, i):
        """
        获取check项的element_info元素
        :param i: 位置序列号
        :return: 返回find_type元素数据
        """
        data = self.alldata()
        return data['check'][i]['find_type']

    def get_CheckOperate_type(self, i):
        data = self.alldata()
        return data['check'][i]['operate_type']

    def dataIncreasing(self, key):
        """数据+1，防止数据重复"""
        with open(self.path, 'r', encoding='utf-8') as f:
            lines = []  # 创建了一个空列表，里面没有元素
            for line in f.readlines():
                if line != '\n':
                    lines.append(line)
            # print(lines)
            f.close()
        with open(self.path, 'w', encoding='utf-8') as f:
            for line in lines:
                if key in line and '#' not in line:
                    number = re.sub('\D', '', line)
                    list = line.split(number)
                    newline = list[0] + str(int(number) + 1) + list[1]
                    f.write('%s' % newline)
                else:
                    f.write('%s' % line)
                # if "userLogin" in line and '#' not in line and "userLogin" in key:
                #     number = re.sub('\D', '', line)
                #     number = int(number) + 1
                #     newline = ' userLogin: "subtest' + str(number) +'"\n'
                #     f.write('%s' % newline)
                # elif "subEmail" in line and '#' not in line and "subEmail" in key:
                #     number = re.sub('\D', '', line)
                #     number = int(number) + 1
                #     newline = ' subEmail: "BSSaddSubAccounttest@qq.com' + str(number) + '"\n'
                #     f.write('%s' % newline)
                # elif "subPhoneNumber" in line and '#' not in line and "subPhoneNumber" in key:
                #     number = re.sub('\D', '', line)
                #     number = int(number) + 1
                #     newline = ' subPhoneNumber: "' + str(number) + '"\n'
                #     f.write('%s' % newline)
                # elif "FacebookID" in line and '#' not in line and "FacebookID" in key:
                #     number = re.sub('\D', '', line)
                #     number = int(number) + 1
                #     newline = ' FacebookID: "test' + str(number) + '"\n'
                #     f.write('%s' % newline)
                # elif "WhatsAppAccount" in line and '#' not in line and "WhatsAppAccount" in key:
                #     number = re.sub('\D', '', line)
                #     number = int(number) + 1
                #     newline = ' WhatsAppAccount: "' + str(number) + '"\n'
                #     f.write('%s' % newline)
                # else:
                #     f.write('%s' % line)
            f.close()

# getyaml("D:\\PycharmProjects\\EEP\\testdata\\uniqueData.yaml").dataIncreasing("WhatsAppAccount")
