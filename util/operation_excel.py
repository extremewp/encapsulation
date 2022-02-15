import xlrd
import yaml
from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name != None:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = "../dataconfig/case1.xls"
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheets信息
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheet_by_index(self.sheet_id)
        return table

    #     获取表格总行数
    def get_lines(self):
        return self.data.nrows

    # 根据 行和列获取表格属性
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        data_read = xlrd.open_workbook(self.file_name)
        write_data = copy(data_read)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应地case_id找到对应行的内容
    def get_row_data(self, case_id):
        row=self.get_row_rum(case_id)
        row_valure = self.get_row_values(row)
        return row_valure

    # 根据对应caseid找到对应行号
    def get_row_rum(self, case_id):
        num =0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num=num+1

    # 根据行号,找到改行地内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列地内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    gt = OperationExcel()
    gt.write_value(1,11,"flass")
