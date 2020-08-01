#coding = utf-8
from selenium import webdriver
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append('E:\programs\pycharmprojects\selenium\pageobject')
from base.read_ini import readIni
class seleniumWebdriver():
    def __init__(self,driver):
        self.driver = driver




    # def wait(self,time,event,check = None):
    #     wait = WebDriverWait(self.driver,time)
    #     if check == None:
    #         wait.until(event)
    #     else:
    #         wait.until_not(event)

    def get_url(self,url):
        if self.driver != None:
            if "http://" or "https://" in url:
                self.driver.get(url)

            else:
                print('请输入正确的url')
        else:
            print("浏览器未打开")

    def window_control(self,*args):
        value =len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'forward':
                self.driver.forward()
            elif args[0] == 'back':
                self.driver.back()
            else:
                elf.driver.refresh()
        elif value == 2:
            self.driver.set_window_size(args[0],args[1])
        else:
            print('输入的参数有误')

    def assert_title(self,title_name = None):
        if title != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def open_url_is_true(self,url,title_name = None):
        self.get_url(url)
        return self.assert_title(title_name)

    def switch_window(self,title_name = None):
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for handle in handles:
            time.sleep(1)
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                if self.assert_title(title_name):
                    break

    def element_is_displayed(self,element):
        flag = element.is_displayed()
        if flag == True:
            return  element
        else:
            return False

    def get_local_element(self,key_name):
        data = readIni.get_value(key_name)
        data_list = data.split('>')
        by = data_list[0]
        value = data_list[1]
        return  by,value

    def get_element(self,key_name):
        data = self.get_local_element(key_name)
        by = data[0]
        value = data[1]
        try:
            if by == 'xpath':
                element = self.driver.find_element_by_xpath(value)
            elif by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'link':
                element = self.driver.find_element_by_link_text(value)
            else:
                element = self.driver.find_element_by_tag_name(value)
            return self.element_is_displayed(element)

        except:
            print('定位方式：',by,'定位值：',value,'定位失败')
            return None


    def get_range_user(self):
        user = ''.join(random.sample('1234567890abcdefghijklmn',8))
        return user

    def close_driver(self):
        self.driver.close()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    demo = seleniumWebdriver(driver)
    demo.get_url('http://www.5itest.cn/register')
    demo.get_element('email').send_keys('1111')
    driver.close()