#coding = utf-8
from key_word.actionMethod import ActionMethod
from base.read_execl import ReadExecl
import time
class KeyWordCase:
    def __init__(self):
        self.action_method = ActionMethod()


    def run_main(self):
        #读入excel表格
        handle_excel = ReadExecl('E:\programs\pycharmprojects\selenium_python\pageobject\config\\keyword.xls')
        #获取表格中有数据的行数
        lines = handle_excel.get_lines()
        #当excel表格不为空时
        if lines:
            #遍历每一行单元格，获取第三列的“是否执行”表格的数据
            for i in range(1,lines):
                is_run = handle_excel.get_col_value(i,3)
                #当第三列不为空，也就是需要执行改行用例
                if is_run:
                    #获取第四列执行方法
                    method = handle_excel.get_col_value(i,4)
                    #获取第五列输入数据
                    value = handle_excel.get_col_value(i,5)
                    #获取第六列操作元素
                    element = handle_excel.get_col_value(i,6)
                    #获取第七列：判断预期结果方法
                    except_result_method = handle_excel.get_col_value(i,7)
                    #获取第八列预期结果值，此时值时一个字符串形式
                    except_result = handle_excel.get_col_value(i,8)
                    #运行该行指定的执行方法
                    self.run_method(method,value,element)
                    #当预期结果值不为空时
                    if except_result != '':
                        #预期结果值的格式"title=注册"
                        #获取预期结果值，并转换为列表形式
                        except_value = self.get_except_result_value(except_result)
                        #当预期结果为title时，此时判断打开url后的页面title与预期结果是否相同，相同则写入pass
                        if except_value[0] == 'title':
                            #获取运行预期结果得到的值
                            result = self.run_method(except_result_method)
                            #当预期结果与预期结果值
                            if except_value[1] in result:
                                handle_excel.write_data(i,'pass')
                            else:
                                handle_excel.write_data(i,'fail')
                        #当预期结果为定位元素时，此时通过运行预期结果中的方法，获取报错信息元素
                        #当元素不为空，表示case成功，写入pass
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_data(i,'pass')
                            else:
                                handle_excel.write_data(i,'fail')

    #将数据依据指定分隔符分隔，返回一个列表
    def get_except_result_value(self,data):
        return data.split('=')

    #通过getattr()方法，运行指定的方法
    def run_method(self,method,value = '',element = ''):
        method_value = getattr(self.action_method,method)
        if value != '' and element != '':
            result = method_value(value,element)
        elif value != '' and element == '':
            result = method_value(value)
        elif value == '' and element != '':
            result = method_value(element)
        else:
            result = method_value()
        return result
if __name__ == '__main__':
    KWC = KeyWordCase()
    KWC.run_main()