#coding = utf-8

import time
import random
import urllib
import urllib.request
import base64
import re
from PIL import Image
from selenium import  webdriver
from base.find_element import seleniumWebdriver
class RegisterCode():
    def __init__(self,driver):
        self.driver = driver

    def get_code_image(self,key_name,file_name):
        find_element = seleniumWebdriver(self.driver)
        self.driver.save_screenshot(file_name)
        code_element = find_element.get_element(key_name)
        left = code_element.location['x']
        top = code_element.location['y']
        right = left + code_element.size['width']
        height = top + code_element.size['height']
        im = Image.open(file_name)
        if self.driver.name == "MicrosoftEdge":
            out = im.resize((1260, 750), Image.ANTIALIAS)
        else:
            out = im.resize((1260,712),Image.ANTIALIAS)
        out.save(file_name)
        image = out.crop((left,top,right,height))
        image.save(file_name)
        time.sleep(2)

    def parsing_code_image(self,file_name):
        host = 'https://codevirify.market.alicloudapi.com'
        path = '/icredit_ai_image/verify_code/v1'
        # 阿里云APPCODE
        appcode = '6b54337f8927480fbfa52c63d49c3505'
        url = host + path
        bodys = {}
        querys = ""

        # 参数配置

        # 启用BASE64编码方式进行识别
        # 内容数据类型是BASE64编码
        f = open(file_name, 'rb')
        contents = base64.b64encode(f.read())
        f.close()
        bodys['IMAGE'] = contents
        bodys['IMAGE_TYPE'] = '0'
        # else:
        #     #启用URL方式进行识别
        #     #内容数据类型是图像文件URL链接
        #     bodys['IMAGE'] = 'https://icredit-api-market.oss-cn-hangzhou.aliyuncs.com/%E9%AA%8C%E8%AF%81%E7%A0%81.jpg'
        #     bodys['IMAGE_TYPE'] = 'case'

        post_data = urllib.parse.urlencode(bodys).encode('utf-8')

        request = urllib.request.Request(url, post_data)
        request.add_header('Authorization', 'APPCODE ' + appcode)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        if (content):
            dict = eval(content.decode('utf-8'))
            time.sleep(2)
            return dict['VERIFY_CODE_ENTITY']['VERIFY_CODE']



    def assert_register(self):
        '''
        通过查找验证码失败后的提示，来确定验证码是否成功
        如果查找到该元素，说明验证码输入错误，循环获取图片，分析图片，输入验证码的流程
        直到查找不到该元素时，说明验证码匹配成功
        :return:
        '''
        find_element = seleniumWebdriver(self.driver)
        value = find_element.get_element('wrong')
        while value != None:
            self.get_code_image('image', 'E:/programs/pycharmprojects/image1.png')
            time.sleep(3)
            text = self.parsing_code_image('E:/programs/pycharmprojects/image1.png')
            print(text)
            time.sleep(3)
            find_element.get_element('captcha').clear()
            find_element.get_element('captcha').send_keys(text)
            find_element.get_element('register').click()


if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    RC = RegisterCode(driver)
    RC.get_code_image('captcha','E:\programs\pycharmprojects\selenium_python\pageobject\image\\test2.png')
    driver.close()