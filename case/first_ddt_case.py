#coding= utf-8
import ddt
import unittest
import time
import os
import HTMLTestRunner
from base.read_execl import ReadExecl
from selenium import webdriver
from business.register_business import RegisterBusiness
RE = ReadExecl()
data = RE.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = "E:/programs/pycharmprojects/selenium_python/pageobject/image/test01.png"

    @classmethod
    def tearDownClass(self):

        print('所有case运行后的后置条件')

    def setUp(self):
        # self.file_name = "E:/programs/pycharmprojects/selenium_python/pageobject/image/test01.png"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get('http://www.5itest.cn/register')
        self.RB = RegisterBusiness(self.driver)


    def tearDown(self):
        # 通过self._outcome.errors捕捉报错信息，并提取其中的值到method_name,error两个变量中
        for method_name, error in self._outcome.errors:
            # 当错误不为空时，执行截图操作，截图文件保存路径为当前工程目录下report文件夹
            # 并以当前case命名
            if error:
                # 获取当前case名称
                case_name = self._testMethodName
                # 设置路径为当前工程目录下report文件夹，并以当前运行case命名的文件
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/report/' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()


    '''
    @ddt.data(
        ['12','12345','123456','code','email_error','请输入有效的电子邮件地址'],
        ['@qq.com','12345','123456','code','email_error','请输入有效的电子邮件地址'],
        ['1234@qq.com', '12345', '123456', 'code', 'email_error', '请输入有效的电子邮件地址']
    )
    '''
    @ddt.data(*data)

    def test_login_register(self,data):
        email, username, password, code, assertCode, assertText=data
        test= self.RB.register_function(email,username,password,code,assertCode,assertText)
        return self.assertFalse(test,'case失败')

if __name__ == '__main__':
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/report/' + 'first_case1.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='th second report',description='这是第二份报告',verbosity=2)
    runner.run(suite)