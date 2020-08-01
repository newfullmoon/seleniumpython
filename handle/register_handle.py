#coding = utf-8
import time
from handle.get_register_image import RegisterCode
from selenium import  webdriver
from page.register_page import GetElement


class RegisterHandle():
    def __init__(self,driver):
        self.GE = GetElement(driver)
        self.RC = RegisterCode(driver)

    def send_email(self,email):
        self.GE.get_email_element().send_keys(email)

    def send_username(self,username):
        self.GE.get_user_name_element().send_keys(username)

    def send_password(self,password):
        self.GE.get_password_element().send_keys(password)

    def send_captcha(self,file_name):
        #captcha_text = self.get_captcha('captcha',file_name)
        self.GE.get_captcha_element().send_keys(file_name)

    def get_user_text(self,info):
        try:
            if info == 'email_error':
                text = self.GE.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.GE.get_user_name_error_element().text
            elif info == 'password_error':
                text = self.GE.get_password_error_element().text
            else:
                text = self.GE.get_captcha_error_element().text
        except:
            text = None
        return text

        
    def click_register_button(self):
        self.GE.get_register_element().click()

    def get_captcha(self,key,filename):

        self.RC.get_code_image(key,filename)
        return self.RC.parsing_code_image(filename)


    def get_register_text(self):
        return self.GE.get_register_element().text

if __name__ == '__main__':
    driver= webdriver.Chrome()
    driver.get('http://www.5itest.cn/register')
    RH = RegisterHandle(driver)
    time.sleep(3)
    RH.send_email('11111')
    RH.click_register_button()
    time.sleep(1)
    print(RH.get_user_text('email_error'))