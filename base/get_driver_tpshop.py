from selenium import webdriver

def get_driver_tpshop():
    driver = webdriver.Firefox()
    driver.get("http://www.tpshop.com/index.php")
    return driver

