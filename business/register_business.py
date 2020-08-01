#coding = utf-8
import sys
sys.path.append('E:\programs\pycharmprojects\selenium\pageobject')
from handle.register_handle import RegisterHandle
from handle.get_register_image import RegisterCode

class RegisterBusiness():
    def __init__(self,driver):
        self.RH = RegisterHandle(driver)



    def user_base(self,email,username,password,file_name):
        self.RH.send_email(email)
        self.RH.send_username(username)
        self.RH.send_password(password)
        self.RH.send_captcha(file_name)
        self.RH.click_register_button()







    def register_function(self,email,username,password,file_name,key,assert_text):
        self.user_base(email,username,password,file_name)
        if self.RH.get_user_text(key) == assert_text:
            return False
        else:
            return True



    def login_email(self,email,username,password,file_name):
        self.user_base(email,username,password,file_name)
        if self.RH.get_user_text('email_error') == '请输入有效的电子邮件地址':
            print('邮箱输入错误')
            return False
        else:
            print('邮箱输入正确')
            return True

    def login_username(self,email,username,password,file_name):
        self.user_base(email,username,password,file_name)
        if self.RH.get_user_text('user_name_error') == '字符长度必须大于等于4，一个中文字算2个字符':
            print('用户名输入错误')
            return  False
        else:
            print('用户名输入正确')
            return True


    def login_password(self,email,username,password,file_name):
        self.user_base(email,username,password,file_name)
        if self.RH.get_user_text('password_error') == '最少需要输入 5 个字符':
            print('密码输入错误')
            return False
        else:
            print('密码输入正确')
            return True


    def login_captcha(self,email,username,password,file_name):
        self.user_base(email,username,password,file_name)
        if self.RH.get_user_text('captcha_error') == '验证码错误':
            print('验证码输入错误')
            return False
        else:
            print('验证码输入正确')
            return True

    def register_success(self,email,username,password,file_name):
        self.user_base(email,username,password,file_name)
        if self.RH.get_register_text() == None:
            return True
        else:
            return False

