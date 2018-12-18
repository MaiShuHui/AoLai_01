from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化
    def __init__(self,driver):
        self.driver = driver
    # 查找方法
    def base_find_element(self,loc,time=30,poll=0.1):
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 输入方法
    def base_input(self,loc,value):
        element = self.base_find_element(loc)
        element.clear()
        element.send_keys(value)
    # 点击方法
    def base_click(self,loc):
        self.base_find_element(loc).click()
    # 获取文本内容方法
    def base_get_text(self,loc):
        return self.base_find_element(loc).text

    # 获取tosat方法
    def base_get_tosat(self, msg):
        loc = By.XPATH, "//*[contains(@text,'" + msg + "')]"
        return self.base_find_element(loc, time=3,poll=0.1).text
    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./image/faild.png")
    # 拖拽方法
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)