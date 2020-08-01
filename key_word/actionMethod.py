#coding = utf-8
from selenium import webdriver
import time
from base.read_ini import readIni
class ActionMethod:


    def open_browser(self,browser):
        if browser == None:
            print('请输入浏览器，支持："chrome","firefox","edge","ie"')
        else:
            if browser == 'chrome':
                options = webdriver.ChromeOptions()
                prefs = {'download.default_directory': 'E:\google\\', 'profile.default_content_setting.popups': 0}
                options.add_experimental_option('prefs', prefs)
                self.driver = webdriver.Chrome(options=options)  # 一定要加括号
            elif browser == 'firefox':
                profile = webdriver.FirefoxProfile()
                # 指定一个浏览器下载路径
                profile.set_preference('browser.download.dir', 'E:\google\\')
                # 设置选择哪一个下载路径，2为自定义路径
                profile.set_preference('browse.dowload.folderList', 2)
                # 设置关闭弹窗
                profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
                self.driver = webdriver.Firefox(firefox_profile=profile)
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                self.driver = webdriver.Ie()


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
            return element

        except:
            print('定位方式：',by,'定位值：',value,'定位失败')
            return None

    def get_url(self,url):


        if self.driver != None:
            if "http://" or "https://" in url:
                self.driver.get(url)

            else:
                print('请输入正确的url')
        else:
            print("浏览器未打开")

    def click_element(self,key_name):
        self.get_element(key_name).click()

    def sleep_time(self,time):
        time.sleep(time)

    def send_value(self,value,key_name):
        self.get_element(key_name).send_keys(value)

    def close_driver(self):
        self.driver.close()

    def get_title(self):
        return  self.driver.title

if __name__ == '__main__':
    AM = ActionMethod()
    AM.open_browser('chrome')

    AM.get_url("http://www.5itest.cn/register")
    # AM.get_element('password')
    AM .send_value('test','password')