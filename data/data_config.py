class global_var:
    Id = 0  # id
    request_name = 1  # 模块
    url = 2  # url
    run = 3  # 是否运行
    request_method = 4 # 请求类型
    request_header = 5  # 是否携带header
    request_case = 6  # case依赖
    request_data_case = 7  # 依赖的返回数据
    request_data_case_file = 8  # 数据依赖字段
    data = 9  # 请求数据
    expect = 10  # 预期结果一
    expect_two = 11# 预期结果二
    result = 12  # 实际结果


def get_id():
    return global_var.Id


def get_request_name():
    return global_var.request_name


def get_url():
    return global_var.url


def get_run():
    return global_var.run


def get_request_method():
    return global_var.request_method


def get_request_header():
    return global_var.request_header


def get_request_case():
    return global_var.request_case


def get_request_data_case():
    return global_var.request_data_case


def get_request_data_case_file():
    return global_var.request_data_case_file


def get_data():
    return global_var.data


def get_expect():
    return global_var.expect


def get_result():
    return global_var.result


def expect_two():
    return global_var.expect_two

def get_header_value():
    header = {
          "token": "j40union_cf7291056a4d2b91e5d37986aba0e45d"
    }
    return header