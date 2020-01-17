from appium import webdriver


def init_driver():
    # 实例化驱动对象
    capabilities = {
        "platformName": "Android",  # 平台名称（Android 或 iOS）
        "platformVersion": "5.1",  # 系统版本
        "deviceName": "模拟器",  # 设备名称
        # 设置 包名/启动名
        "appPackage": "com.bjcsxq.chat.carfriend",  # 待测应用包名
        "appActivity": ".MainActivity",  # 待测应用启动名
        # 解决无法输入中文问题
        "resetKeyboard": True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver


if __name__ == '__main__':
    init_driver()
