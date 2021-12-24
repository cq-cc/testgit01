"""
@File:test_login.py
@DateTime:2021/12/18 16:19
@Author:Ben
@Desc:
"""
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from web_automation.day_07.log.log import logger
from web_automation.day_07.pageobjects.page_login import LoginPage
from web_automation.day_07.config.config import url, driver_path, file, sheet
from web_automation.day_07.data.read_write import ReadWrite


class TestCases(unittest.TestCase):

    def setUp(self):
        logger.info('打开浏览器')
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.page = LoginPage(self.driver)
        self.doc1 = ReadWrite(file, sheet)

        pass

    def tearDown(self):
        logger.info('关闭浏览器')
        self.driver.quit()
        pass

    # 测试用例1
    def test_login_success(self):
        """验证用户名和密码正确登录成功"""
        data_list = self.doc1.read()
        sleep(2)
        self.page.type_username(data_list[0][0])
        self.page.type_password(data_list[0][1])
        self.page.click_login()
        sleep(2)
        try:
            assert self.driver.title == '我的地盘 - 禅道'
            logger.info('验证用户名和密码正确登录成功-----passed')
            self.page.click_logout()
        except:
            logger.info('验证用户名和密码正确登录成功-----failed')
        pass

    # 测试用例2
    def test_login_wrong_password(self):
        """验证密码错误登录失败"""
        data_list = self.doc1.read()
        sleep(2)
        self.page.type_username(data_list[1][0])
        # 3.输入错误的密码
        self.page.type_password(data_list[1][1])
        # 4.点击登录按钮
        self.page.click_login()
        sleep(1)
        try:
            # 断言登录失败的警告框出现
            alert = self.driver.switch_to.alert
            assert "登录失败" in alert.text
            logger.info('验证密码错误登录失败-----passed')
            # alert = Alert(self.driver)
            alert.accept()
        except:
            logger.info('验证密码错误登录失败-----failed')
        pass

    # 测试用例3
    @unittest.skip  # 添加装饰器跳过此测试用例
    def test_login_not_exist(self):
        """验证用户不存在登录失败"""
        data_list = self.doc1.read()
        sleep(2)
        self.page.type_username(data_list[2][0])
        # 3.输入错误的密码
        self.page.type_password(data_list[2][1])
        # 4.点击登录按钮
        self.page.click_login()
        sleep(1)
        try:
            # 断言登录失败的警告框出现
            alert = self.driver.switch_to.alert
            assert "登录失败" in alert.text
            logger.info('验证用户不存在登录失败-----passed')
            # alert = Alert(self.driver)
            alert.accept()
        except:
            logger.info('验证用户不存在登录失败-----failed')
        pass
