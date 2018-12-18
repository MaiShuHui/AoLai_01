import os

import yaml


class ReadYaml():

    def __init__(self,filename):
        self.filename = os.getcwd() + os.sep + "data" + os.sep + filename

    def read_yaml(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return yaml.load(f)

    def read_yaml_01(self):
        with open("../data/al_login_data.yaml", "r", encoding="utf-8") as f:
            return yaml.load(f)


if __name__ == '__main__':
    data = []
    arrs = []
    for data in ReadYaml("al_login_data.yaml").read_yaml_01().values():
        arrs.append((data.get("number"), data.get("password"), data.get("exepect_result"), data.get("expect_tosat")))
    print(arrs)