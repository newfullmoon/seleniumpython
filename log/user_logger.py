#coding = utf-8
import logging
import os
import time
#logging模块实例化，使用getLogger()方法
class UserLog():
    def __init__(self):

        base_dir = os.path.join(os.path.dirname(os.getcwd())+'\\'+'log' + '\\' + 'logs')
        file_name = time.strftime('%Y-%m-%d',time.gmtime())
        log_file = os.path.join(base_dir + '\\' + file_name)
        fmt = '%(asctime)s %(levelno)s %(funcName)s %(levelname)s  %(message)s'

        logging.basicConfig(filename=log_file,level=logging.INFO,format=fmt)


        self.logger = logging.getLogger()





        #设置日志级别
        # self.logger.setLevel(logging.DEBUG)
        #设置日志处理模块，StreamHandler()日志输出到流
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)







        # 设置日志处理模块，FileHandler()日志输出到指定文件，并设置日志的格式
        # self.FH = logging.FileHandler(log_file,mode='a',encoding='utf-8')
        # formatter = logging.Formatter('%(asctime)s' '--' '%(levelno)s' '--' '%(funcName)s ''---->' '%(levelname)s' '--->' '%(message)s')
        # self.FH.setLevel(logging.INFO)
        # self.FH.setFormatter(formatter)
        # self.logger.addHandler(self.FH)
        #


        # logger.debug("test")
        # consle.close()


    def get_log(self):
        return self.logger

    def close_log(self):

        # self.logger.removeHandler(consle)
        self.FH.close()
        self.logger.removeHandler(self.FH)
        self.logger.removeHandler()
        self.logger.removeFilter()


if __name__ == '__main__':
    logger = UserLog()
    log = logger.get_log()
    log.warning('this is test')
