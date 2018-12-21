from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化
    def __init__(self,driver):
        self.driver = driver

    # 查找单个元素方法
    def base_find_element(self,loc,time=30,poll=0.1):
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 查找一组元素方法
    def base_find_elements(self,loc,time=30,poll=0.1):
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_elements(*loc))


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

    # 根据文本,查找元素
    def base_text_get_element(self,text):
        loc = By.XPATH, "//*[contains(@text,'" + text + "')]"
        return self.base_find_element(loc, time=3, poll=0.1)

    # 根据文本,点击元素
    def base_text_click(self,text):
        self.base_text_get_element(text).click()

    # 根据文本 查找一组元素
    def base_text_get_elements(self,text):
        loc = By.XPATH, "//*[contains(@text,'" + text + "')]"
        return self.base_find_elements(loc, time=3, poll=0.1)

    # 传一组元素,默认点击第一个
    def base_click_elements(self,text,num=0):
        self.base_text_get_elements(text)[num].click()

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./image/faild.png")

    # 拖拽方法
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)

