import json

from jsonpath_rw import jsonpath,parse

from base.runmethod import RunMethod
from data.get_data import GetData
from util.operation_excel import OperationExcel



class DependentData:
    def __init__(self, case_id):
        self.operation_excel = OperationExcel()
        self.case_id = case_id
        self.get_data = GetData()

    # 通过case_id 获取改case_id在excel中地整行数据
    def get_case_line_data(self):
        self.operation_excel.get_row_data(self.case_id)

    # 执行依赖测试,获取结果
    def run_dependent(self):
        self.run_method = RunMethod()
        row_num = self.operation_excel.get_row_rum(self.case_id)
        is_url = self.get_data.get_request_url(row_num)
        is_mothod = self.get_data.get_request_mothod(row_num)
        is_header = self.get_data.get_request_header(row_num)
        is_data = self.get_data.get_request_from_user_data(row_num)
        res = self.run_method.run_main(is_mothod, is_url, is_data, is_header)
        return json.loads(res)

    # 根据依赖地key去获取执行依赖测试case地响应,然后返回
    def get_data_for_key(self, row):
        depend_data = self.get_data.get_request_data_case(row)
        response_data = self.run_dependent()
        json_exe=parse('data[*].'+depend_data)
        madle = json_exe.find(response_data)
        data_key=[math.value for math in madle][0]
        return data_key





if __name__ == '__main__':
    ds=DependentData("order_no")
    ds.test_dasd()