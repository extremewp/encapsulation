class CommonUtil:
    # 判断预期值和实际是否一致
    def is_contain(self,str_one,str_two,res):
        flag = None
        if str_one in  res and str_two in res :
            flag = True
        else:
            flag = False
        return flag
