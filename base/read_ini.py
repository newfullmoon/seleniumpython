#coding = utf-8
import  configparser
class ReadIni():
    def __init__(self,path,section_name):
        self.path = path
        self.section_name = section_name
        self.data = self.load_ini()

    def load_ini(self):
        config = configparser.ConfigParser()
        config.read(self.path,encoding='utf-8-sig')
        return  config

    def get_value(self,key):
        return  self.data.get(self.section_name,key)


readIni = ReadIni('E:\programs\pycharmprojects\selenium_python\pageobject\config\element.ini','element')