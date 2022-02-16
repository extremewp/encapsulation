
import pytest
import yaml


class YamlHeader:
    def yaml_header(self):
        data = {"order":{
          "token": "j40union_cf7291056a4d2b91e5d37986aba0e45d"
    },
            "order11":{
                "token": "j40union_cf7291056a4d2b91e5d37986aba0e45d",
                "wqeq":"eqweq"
            }
        }
        with open("../dataconfig/header.yml","w") as f:
            yaml.safe_dump(data=data, stream=f)

if __name__ == '__main__':
        yu=YamlHeader()
        yu.yaml_header()