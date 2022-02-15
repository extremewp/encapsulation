import json

import requests


class RunMethod:
    def post_main(self,url,data=None,header=None):
        res=None
        if header=="no":
            res=requests.post(url=url,data=data)
        else:
            res=requests.post(url=url, data=data, headers=header)
        return res.json()

    def get_main(self,url,data=None,header=None):
        res = None
        if header == None:
            res = requests.get(url=url, params=data)
        else:
            res = requests.get(url=url, params=data, headers=header)
        return res.json()

    def run_main(self,method,url,data=None,header=None):
        res=None
        if method=='Post':
            res=self.post_main(url,data,header)
        else:
            res=self.get_main(url,data,header)
        return json.dumps(res)

