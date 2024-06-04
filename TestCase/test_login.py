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

@allure.feature("测试超级盾登录模块")
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        """打开网址"""
        search = SearchPage(drivers)
        search.get_url(ini.url)



    @allure.story("登录失败case")
    def test_login_01(self, drivers):
        """测试搜索候选"""
        search = SearchPage(drivers)
        search.input_search_name("17379966461")
        search.input_search_password("hj12345")
        search.click_search()

        str = '用户名或密码错误'
        assert str in search.get_infor()

    @allure.story('用户名为空')
    def test_login_02(self, drivers):
        search = SearchPage(drivers)
        search.input_search_name("")
        search.input_search_password("hj123456")
        search.click_search()

        str = '账号不可为空'
        assert str in search.get_search_infor()

    @allure.story('密码为空')
    def test_login_03(self, drivers):
        search = SearchPage(drivers)
        search.input_search_name('17379966461')
        search.input_search_password('')
        search.click_search()

        str = "密码不可为空"
        assert str in search.get_search_infor()

    @allure.story('登录名或密码名不正确')
    def test_login_04(self, drivers):
        search = SearchPage(drivers)
        search.input_search_name('gh123123132')
        search.input_search_password('hj123456')
        search.click_search()

        str = '您输入的账号有误，您的帐号可能是您的手机号'
        assert str == search.get_search_infor()

if __name__ == '__main__':
    pytest.main(['-sv', 'test_login.py', '--alluredir=./allure'])
    os.system('allure serve allure')
