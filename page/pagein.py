from base.get_driver import get_driver
from page.page_address import PageAddress
from page.page_aolai import PageAolai


class PageIn():
    #  百年奥莱登录页面
    def get_al_login(self):
        driver = get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        return PageAolai(driver)

    # 百年奥莱地址管理页面
    def get_address(self):
        driver = get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        return PageAddress(driver)
