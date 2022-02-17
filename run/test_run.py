import sys
sys.path.append("D:\Develop\encapsulation")
from base.runmethod import RunMethod
from data import data_config
from data.dependent_data import DependentData
from data.get_data import GetData
from util.common_util import CommonUtil
from util.operation_excel import OperationExcel


class TestRun:
    def __init__(self):
        self.run_method=RunMethod()
        self.get_data=GetData()
        self.common_util = CommonUtil()
        self.operation_excel = OperationExcel()

    def test_run(self):
        res =None
        rows_count = self.get_data.get_request_lines()
        pass_count=[]
        fail_count=[]
        for i in range(1,rows_count):
            is_run = self.get_data.get_request_run(i)
            if is_run :
                is_url = self.get_data.get_request_url(i)
                is_mothod = self.get_data.get_request_mothod(i)
                is_header = self.get_data.get_request_header(i)
                is_data = self.get_data.get_request_from_user_data(i)
                is_str_one = self.get_data.get_request_expcel(i)
                is_str_two = self.get_data.get_request_expcel_two(i)
                is_case = self.get_data.get_request_case(i)
                if is_case == None:
                    res = self.run_method.run_main(is_mothod, is_url, is_data, is_header)
                    print(res)
                    test_values = None
                    if self.common_util.is_contain(is_str_one,is_str_two, res):
                        test_values = "pass"
                        self.operation_excel.write_value(i, data_config.get_result(), test_values)
                        print("通过")
                        pass_count.append(i)
                    else:
                        test_values = res
                        self.operation_excel.write_value(i, data_config.get_result(), test_values)
                        fail_count.append(i)
                        print("未通过")
                else:
                    dependent_data = DependentData(is_case)
                    # 获取的依赖响应数据
                    depend_request_data = dependent_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.get_data.get_request_data_case_file(i)
                    is_data[depend_key]=depend_request_data

                    # (self,method,url,data=None,header=None)
                    res = self.run_method.run_main(is_mothod, is_url, is_data, is_header)
                    print(res)
                    test_values = None
                    if self.common_util.is_contain(is_str_one,is_str_two, res):
                        test_values = "pass"
                        self.operation_excel.write_value(i, data_config.get_result(), test_values)
                        print("通过")
                        pass_count.append(i)
                    else:
                        test_values = res
                        self.operation_excel.write_value(i, data_config.get_result(), test_values)
                        print("未通过")
                        fail_count.append(i)
        print(len(pass_count))
        print(len(fail_count))

if __name__ == '__main__':
    tr=TestRun()
    tr.test_run()











