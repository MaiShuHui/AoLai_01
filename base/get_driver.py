from appium import webdriver


def get_driver(Package='com.android.settings',Activity='.Settings'):  #默认启动设置页面
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 指定appium库
    desired_caps['automationName'] = 'uiautomator2'
    # app信息
    desired_caps['appPackage'] = Package
    desired_caps['appActivity'] = Activity
    # 输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 获取driver
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
