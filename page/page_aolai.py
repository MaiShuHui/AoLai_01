import allure

import page
from base.base import Base


class PageAolai(Base):
    # 点击 我
    @allure.step("点击 我")
    def page_click_wo(self):
        self.base_click(page.al_wo)

    # 点击 账号登录
    @allure.step("点击 已有账号登录")
    def page_click_zh(self):
        self.base_click(page.al_zh)

    # 输入账号
    @allure.step("输入账号")
    def page_input_number(self,number):
        self.base_input(page.al_number,number)

    # 输入密码
    @allure.step("输入密码")
    def page_input_password(self,password):
        self.base_input(page.al_password,password)

    # 点击登录按钮
    @allure.step("点击 登录按钮")
    def page_click_login_btn(self):
        self.base_click(page.al_btn)

    # 获取昵称
    @allure.step("获取昵称")
    def page_get_text(self):
        return self.base_get_text(page.al_username)

    # 点击设置按钮
    @allure.step("点击 设置按钮")
    def page_click_setting(self):
        self.base_click(page.al_setting)

    # 拖拽 消息推送 至 修改密码
    @allure.step("拖拽 消息推送 至 修改密码")
    def page_drag_and_drop(self):
        el1 = self.base_find_element(page.al_pust)
        el2 = self.base_find_element(page.al_log_pwd)
        self.base_drag_and_drop(el1,el2)

    # 点击退出按钮
    @allure.step("点击 退出登录按钮")
    def page_click_logout(self):
        self.base_click(page.al_click_logout)

    # 点击确认退出
    @allure.step("点击 确认退出")
    def page_click_logout_ok(self):
        self.base_click(page.al_logout_ok)

    # 封装退出登录当前账号方法
    def page_drop_out(self):
        self.page_drag_and_drop()
        self.page_click_logout()
        self.page_click_logout_ok()

    # 定位获取首页购物车文本元素
    @allure.step("获取页面购物车文本内容")
    def page_get_gw_text(self):
        return self.base_get_text(page.al_gw)

    # 封装登录模块
    def page_login(self,number="13318041502",password="123456"):
        self.page_click_wo()
        self.page_click_zh()
        self.page_input_number(number)
        self.page_input_password(password)
        self.page_click_login_btn()
        self.page_click_setting()