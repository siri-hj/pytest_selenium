#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium_pytest.page.webpage import WebPage, sleep
from selenium_pytest.common.readelement import Element

search = Element('search')


class SearchPage(WebPage):
    """搜索类"""

    def input_search_name(self, content):
        """用户名输入"""
        self.input_text(search['超级盾用户名'], txt=content)
        sleep()

    def input_search_password(self, content):
        """密码输入"""
        self.input_text(search['超级盾密码'], txt=content)
        sleep()

    def input_search_text(self, content):
        self.input_text(search['搜索框输入'], txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(search['候选'])]

    def click_search(self):
        """点击确认"""
        self.is_click(search['超级盾按钮'])


    '''页面展示定位'''
    def click_page_button1(self):
        self.is_click(search['产品与功能'])

    def click_page_button2(self):
        self.is_click(search['续费管理'])

    def click_page_button3(self):
        self.is_click(search['订单列表'])

    def click_page_button4(self):
        self.is_click(search['财务管理'])

    def click_page_button4_1(self):
        self.is_click(search['财务管理-费用账单'])

    def click_page_button4_2(self):
        self.is_click(search['财务管理-费用分析'])

    def click_page_button5(self):
        self.is_click(search['合同管理'])

    def click_page_button6(self):
        self.is_click(search['备案管理'])

    def click_page_button7(self):
        self.is_click(search['帮助中心'])

    def click_kongzhitai(self):
        """点击控制台"""
        self.is_click(search['点击控制台'])

    def get_infor(self):
        """获取弹窗错误信息"""
        return self.element_text(search['弹窗提示错误信息'])

    def get_search_infor(self):
        """获取输入框错误信息"""
        return self.element_text(search['输入框提示错误信息'])