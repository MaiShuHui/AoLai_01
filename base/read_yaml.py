import os

import yaml


class ReadYaml():

    def __init__(self,filename):
        self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    def read_yaml(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return yaml.load(f)

    def read_yaml_01(self):
        with open("../data/address.yaml", "r", encoding="utf-8") as f:
            return yaml.load(f)


if __name__ == '__main__':
    arrs = []
    for data in ReadYaml("address.yaml").read_yaml_01().values():
        arrs.append((data.get("name"), data.get("phone"), data.get("province"), data.get("city")
                        , data.get("area"), data.get("address_info"), data.get("code")))
    print(arrs)