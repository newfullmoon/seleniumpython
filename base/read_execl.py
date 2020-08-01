#coding = utf-8
import xlrd
from xlutils import copy
class ReadExecl:
    def __init__(self,execl_path = None,index = None):
        if execl_path == None:
            self.execl_path = "E:\programs\pycharmprojects\selenium_python\pageobject\config\\casedata.xls"
        else:
            self.execl_path = execl_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.execl_path)
        self.table = self.data.sheets()[index]
        self.rows = self.table.nrows

    #获取所有单元格中的值
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return  result

    #获取单元格行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None
    #获取指定单元格的值
    def get_col_value(self,row,col):
        if self.get_lines() > row:
            data = self.table.cell(row,col).value
            return data
        return None
    #向指定单元格中写入数据
    def write_data(self,row,value):
        read_value = xlrd.open_workbook(self.execl_path)
        write_value = copy.copy(read_value)
        write_value.get_sheet(0).write(row,9,value)
        write_value.save(self.execl_path)




if __name__ == '__main__':
    RE = ReadExecl('E:\programs\pycharmprojects\selenium_python\pageobject\config\\keyword.xls')

    print(RE.get_col_value(1,6))
