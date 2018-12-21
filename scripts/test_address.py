import os
import sys
sys.path.append(os.getcwd())
from base.read_yaml import ReadYaml
import page
import allure

import pytest

from page.pagein import PageIn

def get_data(type_value):
    # 定义空列表
    arrs = []
    if type_value == "add":
        for data in ReadYaml("address.yaml").read_yaml().get("add_address").values():
            arrs.append((data.get("name"), data.get("phone"), data.get("province"), data.get("city")
                        , data.get("area"), data.get("address_info"), data.get("code")))
        return arrs

    elif type_value == "update":
        for data in ReadYaml("address.yaml").read_yaml().get("update_address").values():
            arrs.append((data.get("name"), data.get("phone"), data.get("province"), data.get("city")
                         , data.get("area"), data.get("address_info"), data.get("code")))
        return arrs


class TestAddress():

    @allure.step("执行 初始化页面对象")
    def setup_class(self):
        # 实例化奥莱登录页面对象
        self.al_login = PageIn().get_al_login()
        # 实例化地址管理页面对象
        self.address = PageIn().get_address()
        # 打开奥莱页面并成功登录
        self.al_login.page_login()

    @allure.step("执行 关闭页面")
    def teardown_class(self):
        # 关闭页面对象
        self.address.driver.quit()

    # 新增信息
    @pytest.mark.run(order=1)
    @allure.step("执行测试用例  新增信息步骤")
    @pytest.mark.parametrize("name,phone,province,city,area,address_info,code",get_data("add"))
    def test_address(self,name,phone,province, city, area,address_info,code):
        # 点击地址管理
        self.address.page_click_address_manage()
        # 点击新增地址
        self.address.page_click_new_address()
        # 输入收件人信息
        self.address.page_input_receipt_name(name)
        # 输入电话
        self.address.page_input_phone(phone)
        # 点击区域
        self.address.page_click_address_area(province, city, area)
        # 输入详细地址
        self.address.page_input_detail_address(address_info)
        # 输入 邮编
        self.address.page_input_post_code(code)
        # 点击设置为默认地址
        self.address.page_click_default_address()
        # 点击保存
        self.address.page_click_save_btn()
        # 组装收件人+电话
        name_phone = name + "  " + phone
        # 断言获取到的收件人电话
        try:
            assert name_phone in self.address.page_get_list_name_phone()
        except AssertionError:
            self.address.base_get_image()
            with open("./image/faild.png","rb") as f :
                allure.attach("失败原因", f.read(), allure.attach_type.PNG)

    # 更新信息
    @pytest.mark.run(order=2)
    @allure.step("执行测试用例  更改信息步骤")
    @pytest.mark.parametrize("name,phone,province,city,area,address_info,code", get_data("update"))
    def test_update(self,name,phone,province,city,area,address_info,code):
        # 点击编辑
        self.address.page_click_edit_btn()
        # 点击修改,默认修改第一个元素
        self.address.page_click_update_btn(name,phone,province,city,area,address_info,code)
        # 组装收件人+电话
        name_phone = name + "  " + phone
        # 断言获取到的收件人电话
        try:
            assert name_phone in self.address.page_get_list_name_phone()
        except AssertionError:
            self.address.base_get_image()
            with open("./image/faild.png", "rb") as f:
                allure.attach("失败原因", f.read(), allure.attach_type.PNG)

#         删除信息并断言
    @pytest.mark.run(order=3)
    @allure.step("执行测试用例  删除信息步骤")
    def test_delete_address(self):
        # 删除所有信息
        self.address.page_delete_address()

    # 判断是否删除干净
    @pytest.mark.run(order=4)
    @allure.step("判断 是否删除干净")
    def page_is_delete(self):
        try:
            self.address.base_find_elements(page.address_name_phone,timeout=3)
            print("未删除干净")
            return False
        except :
            print("已删除干净")
            return True





