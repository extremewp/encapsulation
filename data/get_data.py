from data import data_config
from util.common_util import CommonUtil
from util.operation_excel import OperationExcel
from util.operation_user import OperationUser


class GetData:
    # 初始化加载OperationExcel()类
    def __init__(self):
        self.oper_excel = OperationExcel()
        self.common_util = CommonUtil()

    # 获取excel表中地行数
    def get_request_lines(self):
        print(self.oper_excel.get_lines())
        return self.oper_excel.get_lines()

    # 获取excel表中地url
    def get_request_url(self, row):
        col = data_config.get_url()
        return self.oper_excel.get_cell_value(col=col, row=row)

    # 判断excel中是否执行这条用例
    def get_request_run(self, row):
        col = data_config.get_run()
        data_run = self.oper_excel.get_cell_value(row=row, col=col)

        if data_run == 'yes':
            return True
        else:
            return False

    # 获取mothod是post还是get
    def get_request_mothod(self, row):
        col = data_config.get_request_method()
        return self.oper_excel.get_cell_value(row=row, col=col)

    # 判断header是否为空
    def get_request_header(self, row):
        col = data_config.get_request_header()
        header = self.oper_excel.get_cell_value(row=row, col=col)
        if header == 'yes':
            header = data_config.get_header_value()
        else:
            header = None
        return header

    # 获取excel中data名字
    def get_request_data(self, row):
        col = data_config.get_data()
        data = self.oper_excel.get_cell_value(row=row, col=col)
        if data == '':
            data = None
        else:
            data = data
        return data

    # 获取user.yml文件中数据
    def get_request_from_user_data(self, row):
        operat_user = OperationUser()
        return operat_user.get_user_data(self.get_request_data(row))

    # 获取excel中预期值
    def get_request_expcel(self, row):
        col = data_config.get_expect()
        return self.oper_excel.get_cell_value(row, col)

    # 获取excel中是否有case
    def get_request_case(self,row):
        col = data_config.get_request_case()
        case =  self.oper_excel.get_cell_value(row, col)
        if   case=='':
            case = None
        else:
            case = case
        return case

    # 获取excel中依赖返回数据值
    def get_request_data_case(self, row):
        col = data_config.get_request_data_case()
        case_data_id = self.oper_excel.get_cell_value(row, col)
        if case_data_id =='':
            return None
        else:
            return case_data_id

    # 获取excel中数据依赖字段
    def get_request_data_case_file(self, row):
        col = data_config.get_request_data_case_file()
        data = self.oper_excel.get_cell_value(row, col)
        if data =='':
            return None
        else:
            return data


