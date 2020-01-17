"""
登录页面
"""

import page

from base.base_page import BasePage


class LoginPage(BasePage):
    phone_num = page.phone_num
    pwd = page.pwd
    login_btn = page.login_btn
    alert_btn = page.alert_btn

    def input_phone_num(self, num):
        """输入手机号码方法"""
        self.input_func(self.phone_num, num)

    def input_pwd(self, pwd):
        """输入密码方法"""
        self.input_func(self.pwd, pwd)

    def click_login_btn(self):
        """点击登录按钮方法"""
        self.click_func(self.login_btn)

    def click_alert_btn(self):
        """点击弹窗确定按钮方法"""
        self.click_func(self.alert_btn)

    def login_func(self, num, pwd):
        """登录操作方法"""
        self.input_phone_num(num)  # 输入手机号码
        self.input_pwd(pwd)   # 输入密码
        self.click_login_btn()  # 点击登录按钮
        self.click_alert_btn()  # 点击登录弹窗按钮
