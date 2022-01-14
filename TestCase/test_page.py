#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
import pytest
import allure
from selenium_pytest.utils.logger import log
from selenium_pytest.common.readconfig import ini
from selenium_pytest.page_object.searchpage import SearchPage
import time

@allure.feature("测试超级盾搜索模块")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        '''打开超级云'''
        search = SearchPage(drivers)
        search.get_url(ini.url)




    @allure.story("页面功能")
    def test_search1(self, drivers):
        '''产品与功能'''
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  #点击登录
        time.sleep(0.5)
        search.click_page_button1()   #产品与功能
        drivers.save_screenshot(r'E:\web\t1.png')


    @allure.story("页面功能")
    def test_search2(self, drivers):
        '''续费管理'''
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  #点击登录
        time.sleep(0.5)
        search.click_page_button2()   #续费管理
        drivers.save_screenshot(r'E:\web\t2.png')
        url = '/layout/renewalManage'
        assert url in drivers.current_url

    @allure.story("页面功能")
    def test_search3(self, drivers):
        '''订单列表'''
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  # 点击登录
        time.sleep(0.5)
        search.click_page_button3()  # 续费管理
        drivers.save_screenshot(r'E:\web\t3.png')

        url = '/layout/billList/listView'
        assert url in drivers.current_url

    @allure.story("页面功能")
    def test_search4(self, drivers):
        '''财务管理'''
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  # 点击登录
        time.sleep(0.5)
        search.click_page_button4()  # 财务管理
        drivers.save_screenshot(r'E:\web\t4.png')

    @allure.story("页面功能")
    def test_search4_1(self, drivers):
        '''财务管理-费用账单'''
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  # 点击登录
        time.sleep(0.5)
        search.click_page_button4()  # 财务管理
        search.click_page_button4_1()  # 财务管理-费用账单
        drivers.save_screenshot(r'E:\web\t4_1.png')

        url = '/layout/finacialManage/feeBill'
        assert url in drivers.current_url

    @allure.story("页面功能")
    def test_search4_2(self, drivers):
        """财务管理-费用分析"""
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  # 点击登录
        time.sleep(0.5)
        search.click_page_button4()  # 财务管理
        search.click_page_button4_2()  # 续费管理
        drivers.save_screenshot(r'E:\web\t4_2.png')

        url = '/layout/finacialManage/feeAnalysis'

        assert url in drivers.current_url

    @allure.story("页面功能")
    def test_search5(self, drivers):
        '''合同管理'''
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  # 点击登录
        time.sleep(0.5)
        search.click_page_button5()  # 续费管理
        drivers.save_screenshot(r'E:\web\t5.png')

        url = '/layout/ContractManage'
        assert url in drivers.current_url

    @allure.story("页面功能")
    def test_search6(self, drivers):
        '''备案管理'''
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  # 点击登录
        time.sleep(0.5)
        search.click_page_button6()  # 续费管理
        drivers.save_screenshot(r'E:\web\t6.png')
        url = '/layout/recordManage'

        assert url in drivers.current_url

    @allure.story("页面功能")
    def test_search7(self, drivers):
        '''帮助中心'''
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj123456")
        search.click_search()  # 点击登录
        time.sleep(0.5)
        search.click_page_button7()  # 续费管理

        drivers.save_screenshot(r'E:\web\t7.png')
        url = '/layout/help'

        assert url in drivers.current_url