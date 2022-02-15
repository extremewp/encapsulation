import pytest
import yaml


class YamlCookie:
    def yaml_cookie(self):
        data = {"loginstate": "1", "apsid": "M5M2Q3YzBkOGVjYzdkYzE3OTM4M2IwYzIwYjRkMWYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTI0OTE5MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGUzOTEwYmVjMWE4ODhiZDk3MTU5ZTA4NzRlNTgzMGJlGqzsWRqs7Fk%3DMG", "imooc_isnew_ct": "1508682778", "cvde": "59ecac1ab3389-1", "imooc_isnew": "1", "PHPSESSID": "kgai3710p58s48cicq0oklku42", "imooc_uuid": "544b2bee-5d3a-4f9c-bcee-68644641de26"}
        with open("./cookie.yml","w") as f:
            yaml.safe_dump(data=data, stream=f)

if __name__ == '__main__':
        yu=YamlCookie()
        yu.yaml_cookie()