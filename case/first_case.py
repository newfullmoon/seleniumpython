#coding = utf-8
import time
import os
import HTMLTestRunner
from selenium import webdriver
from business.register_business import RegisterBusiness
from log.user_logger import UserLog
import unittest

class FirstCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.file_name = "E:/programs/pycharmprojects/selenium_python/pageobject/image/test01.png"
		cls.log = UserLog()
		cls.logger = cls.log.get_log()

	@classmethod
	def tearDownClass(self):
		# self.log.close_log()

		print('所有case运行后的后置条件')

	def setUp(self):
		# self.file_name = "E:/programs/pycharmprojects/selenium_python/pageobject/image/test01.png"
		self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\\chromedriver.exe')
		self.driver.maximize_window()

		time.sleep(2)

		self.driver.get('http://www.5itest.cn/register')
		self.logger.info('this is chrome')

		self.RB = RegisterBusiness(self.driver)

	def tearDown(self):
		#通过self._outcome.errors捕捉报错信息，并提取其中的值到method_name,error两个变量中
		for method_name,error in self._outcome.errors:
			#当错误不为空时，执行截图操作，截图文件保存路径为当前工程目录下report文件夹
			#并以当前case命名
			if error:
				#获取当前case名称
				case_name = self._testMethodName
				#设置路径为当前工程目录下report文件夹，并以当前运行case命名的文件
				file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/report/' + case_name + '.png')
				self.driver.save_screenshot(file_path)
		self.driver.close()




	def test_login_email_error(self):
		email = self.RB.login_email('11111','2222','3333',self.file_name)
		return self.assertFalse(email,'邮箱错误case成功')


	def test_login_uaser_name_error(self):
		username =self.RB.login_username('1234567@163.com','111','123456',self.file_name)
		return self.assertFalse(username,'用户名错误case成功')


	def test_login_password_error(self):
		password =self.RB.login_password('1234567@163.com','111','123',self.file_name)
		return self.assertFalse(password,'密码错误case成功')


	def test_login_code_error(self):
		captcha =self.RB.login_captcha('1234567@163.com','111','123456',self.file_name)
		return self.assertFalse(captcha,'验证码错误case成功')



	def test_login_success(self):
		success = self.RB.register_success('123455655@163.com','12345','12345',self.file_name)
		self.assertTrue(success,'注册成功的case失败')

if  __name__ == '__main__':

	unittest.main()
	#获取当前文键所在目录的工程目录，并在该目录下新建文件夹report，并新建html文件first_case.html
	# file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/report/' + 'first_case.html')
	# f = open(file_path,'wb')
	# 实例化unittest.TestSuite()方法
	# suite = unittest.TestSuite()
	# 将我们想要单独执行的case放入容器suite中
	# tests = {FirstCase('test_login_code_error'),FirstCase('test_login_success')}
	# suite.addTests(tests)
	# 实例化HTMLTestRunner方法，设置参数，stream为打开的html文件
	# runner = HTMLTestRunner.HTMLTestRunner(stream =f,title = "this is first report",description="这是第一份报告",verbosity=2)
	# 用设置好的实例化的HTMLTestRunner方法调用容器
	# runner.run(suite)
# tests1 = (FirstCase('test_login_code_error'), FirstCase('test_login_success'))
# tests2 = [FirstCase('test_login_code_error'), FirstCase('test_login_success')]
	# unittest.TextTestRunner().run(suite)