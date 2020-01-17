"""
首页页面
"""
import page

from base.base_page import BasePage


class IndexPage(BasePage):
    mine = page.mine

    def click_mine(self):
        """点击我的页面方法"""
        self.click_func(self.mine)


