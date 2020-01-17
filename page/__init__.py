from selenium.webdriver.common.by import By

# 首页页面
mine = By.XPATH, '//*[contains(@text, "我的")]'  # 我的

# 我的页面
login_reg = By.XPATH, '//*[contains(@text, "登录")]'  # 登录注册

# 登录页面
phone_num = By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et'  # 手机号码
pwd = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'  # 密码
login_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'  # 登录按钮
alert_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/btn_neg'  # 弹窗确定按钮
