#coding = utf-8
from selenium import  webdriver

from base.find_element import seleniumWebdriver
class GetElement():
    def __init__(self,driver):
        self.selweb = seleniumWebdriver(driver)



    def get_email_element(self):
        return self.selweb.get_element('email')

    def get_user_name_element(self):
        return self.selweb.get_element('username')

    def get_password_element(self):
        return self.selweb.get_element('password')

    def get_captcha_element(self,):
        return self.selweb.get_element('captcha')

    def get_image_element(self):
        return self.selweb.get_element('image')

    def get_register_element(self):
        return self.selweb.get_element('register_button')

    def get_email_error_element(self):
        return self.selweb.get_element('email_error')

    def get_user_name_error_element(self):
        return self.selweb.get_element('username_error')

    def get_password_error_element(self):
        return self.selweb.get_element('password_error')

    def get_captcha_error_element(self):
        return self.selweb.get_element('captcha_error')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.5itest.cn/register')
    GE = GetElement(driver)
    print(GE.get_email_element())
    driver.close()