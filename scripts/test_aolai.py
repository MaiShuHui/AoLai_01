import os
import sys
sys.path.append(os.getcwd())
import page
import allure
import pytest
from base.read_yaml import ReadYaml
from page.pagein import PageIn

def get_data():
    arrs = []
    for data in ReadYaml("al_login_data.yaml").read_yaml().values():
        arrs.append((data.get("number"),data.get("password"),data.get("exepect_result"),data.get("expect_tosat")))
    return arrs

class TestAolai():

    def setup_class(self):
        # 调用实例对像
        self.login = PageIn().get_al_login()
        login = self.login
        # 点击我
        login.page_click_wo()
        # 点击已有账号登录
        login.page_click_zh()

    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("number,password,exepect_result,expect_tosat", get_data())
    def test_aolai(self,number,password,exepect_result,expect_tosat):
        login = self.login

        if exepect_result:
            try:
                # 输入账号
                login.page_input_number(number)
                # 输入密码
                login.page_input_password(password)
                # 点击登录
                login.page_click_login_btn()
                # 查找昵称并断言
                assert exepect_result in login.page_get_text()
                # 登录成功后 点击进入设置页面
                login.page_click_setting()
                # 点击退出当前登录账号
                login.page_drop_out()
                # 断言是否成功退出
                try:
                    assert "购物车" in login.page_get_gw_text()
                    print("成功退出")
                except AssertionError:
                    # 截图
                    login.base_get_image()
                    # 打开图片
                    with open("./image/faild.png", "rb") as f:
                        # 写入报告
                        allure.attach("失败原因", f.read(), allure.attach_type.PNG)
                # 点击我
                login.page_click_wo()
                # 点击已有账号登录
                login.page_click_zh()
            except AssertionError:
                # 截图
                login.base_get_image()
                # 打开图片
                with open("./image/faild.png", "rb") as f:
                # 写入报告
                    allure.attach("失败原因", f.read(), allure.attach_type.PNG)

        else:
            try:
                # 输入账号
                login.page_input_number(number)
                # 输入密码
                login.page_input_password(password)
                # 点击登录
                login.page_click_login_btn()
                # 查找tosat消息并断言
                assert expect_tosat in login.base_get_tosat(expect_tosat)
                # 登录失败,获取tosat消息
            except:
                # 截图
                login.base_get_image()
                # 打开图片
                with open("./image/faild.png","rb") as f:
                # 写入报告
                    allure.attach("失败原因",f.read(),allure.attach_type.PNG)





