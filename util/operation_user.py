import yaml


class OperationUser:

    def __init__(self,file_name=None):
        if file_name == None:
            self.file_name = "../dataconfig/user.yml"
        else:
            self.file_name =None
        self.data=self.read_data(self.file_name)

    def read_data(self,file_name):
        return yaml.safe_load(open(file_name))

    def get_user_data(self,id):
        return self.data[id]

