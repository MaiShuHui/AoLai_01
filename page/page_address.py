import allure

import page
from base.base import Base


class PageAddress(Base):

    # 点击 地址管理
    @allure.step("点击 地址管理")
    def page_click_address_manage(self):
        self.base_click(page.address_manage)

    # 点击 新增地址
    @allure.step("点击 新增地址")
    def page_click_new_address(self):
        self.base_click(page.address_add_new_btn)

    # 输入收件人
    @allure.step("输入 收件人")
    def page_input_receipt_name(self, name):
        self.base_input(page.address_receipt_name, name)

    # 输入电话
    @allure.step("输入 电话")
    def page_input_phone(self, phone):
        self.base_input(page.address_add_phone, phone)

    # 点击 区域
    @allure.step("点击 区域")
    def page_click_address_area(self, province, city, area):
        # 点击 区域
        self.base_click(page.address_area)
        # 省 非直辖市
        self.base_text_click(province)
        # 市
        self.base_text_click(city)
        # 区
        self.base_text_click(area)

    # 输入 详细地址
    @allure.step("输入 详细地址")
    def page_input_detail_address(self, address_info):
        self.base_input(page.address_detail_addr_info, address_info)

    # 输入 邮编
    @allure.step("输入 收件人")
    def page_input_post_code(self, code):
        self.base_input(page.address_post_code, code)

    # 点击 设为默认地址
    @allure.step("点击 设为默认地址")
    def page_click_default_address(self):
        self.base_click(page.address_default)

    # 点击 保存
    @allure.step("点击 保存")
    def page_click_save_btn(self):
        self.base_click(page.address_save)

    # 获取地址列表所有的收件人和电话
    @allure.step("获取 地址列表所有的收件人和电话")
    def page_get_list_name_phone(self):
        element = self.base_find_elements(page.address_name_phone)
        return [el.text for el in element]

    # 点击编辑
    @allure.step("点击 编辑")
    def page_click_edit_btn(self,text="编辑"):
        self.base_text_click(text)

    # 点击修改 默认点击第一个修改元素
    @allure.step("点击 修改,默认点击第一个修改元素")
    def page_click_update_btn(self,name,phone,province,city,area,address_info,code):
        # 点击修改
        self.base_click_elements("修改")
        # 输入收件人
        self.page_input_receipt_name(name)
        # 输入电话
        self.page_input_phone(phone)
        # 点击区域
        self.page_click_address_area(province,city,area)
        # 输入详细地址
        self.page_input_detail_address(address_info)
        # 输入邮编
        self.page_input_post_code(code)
        # 点击保存
        self.page_click_save_btn()
    # 确认删除
    @allure.step("确认 删除")
    def page_click_delete_ok(self):
        self.base_click(page.address_delete_ok)

    # 删除所有地址列表
    @allure.step("删除 所有地址列表")
    def page_delete_address(self):
        # 获取列表长度
        for a in range(len(self.page_get_list_name_phone())):
            # 点击编辑
            self.page_click_edit_btn()
            # 获取删除, 并点击
            self.base_click_elements("删除")
            # 确认删除
            self.page_click_delete_ok()
