class CommonUtil:
    # 判断预期值和实际是否一致
    def is_contain(self,str_one,str_two):
        flag = None
        if str_one in  str_two :
            flag = True
        else:
            flag = False
        return flag
