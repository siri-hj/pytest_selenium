#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
import pytest
import allure
from selenium_pytest.utils.logger import log
from selenium_pytest.common.readconfig import ini
from selenium_pytest.page_object.searchpage import SearchPage
from selenium_pytest.utils.open_url import OpenUrl
import time
from selenium import webdriver


@allure.feature("测试超级盾登录模块")
class TestWeb:
    @pytest.fixture(scope='function', autouse=True)
    def open_chaojiyun(self):
        """打开超级云"""
        print('打开测试')


    @allure.story("测试网页跳转")
    def test_web(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.get('https://cloud.chaojidun.com/login')
        zh = browser.find_element_by_class_name("el-input__inner")
        pwd = browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/input")

        zh.send_keys('17379966461')
        pwd.send_keys('hj123456')

        button = browser.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[2]/div[2]/div[1]/div/button[1]")
        button.click()


        url = [
            "https://cloud.chaojidun.com/layout/productList?redirectUrl=https%3A%2F%2Flive4service.console.aliyun.com",
            "https://cloud.chaojidun.com/layout/productList?redirectUrl=https%3A%2F%2Fyundun4service.console.aliyun.com%2F%3Fp%3Dwaf",
            "https://cloud.chaojidun.com/layout/productList?redirectUrl=https%3A%2F%2Fyundun4service.console.aliyun.com%2F%3Fp%3Dsas"]

        for i in range(len(url)):
            browser = OpenUrl(browser, url[i], i)
            time.sleep(1)

        # 关闭浏览器
        time.sleep(5)
        browser.quit()
