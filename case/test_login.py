"""
登录测试页面
"""
import time

import pytest

from page.page_factory import PageFactory
from utils import init_driver


class TestLogin(object):
    """登录测试类"""

    @pytest.fixture(autouse=True)
    def before_func(self):
        """前置操作"""
        self.driver = init_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)

        yield
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        """登录测试方法"""
        # self.page_factory.index_page().click_mine()  # 点击我的
        # self.page_factory.mine_page().click_login_reg()  # 点击登录注册
        # self.page_factory.login_page().input_phone_num('15570925914')  # 输入手机号码
        # self.page_factory.login_page().input_pwd('qwer123456789')  # 输入密码
        # self.page_factory.login_page().click_login_btn()  # 点击登录按钮
        # self.page_factory.login_page().click_alert_btn()  # 点击弹窗按钮

        self.page_factory.index_page().click_mine()  # 点击我的
        self.page_factory.mine_page().click_login_reg()  # 点击登录注册
        self.page_factory.login_page().login_func('15570925914', 'qwer123456789')  # 登录操作