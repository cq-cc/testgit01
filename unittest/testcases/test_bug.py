"""
@File:test_bug.py
@DateTime:2021/12/18 16:57
@Author:Ben
@Desc:
"""
import unittest
from time import sleep

import win32con
import win32gui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from web_automation.day_07.log.log import logger
from web_automation.day_07.pageobjects.page_login import LoginPage
from web_automation.day_07.config.config import url, driver_path, file, sheet
from web_automation.day_07.data.read_write import ReadWrite


class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info('打开浏览器')
        s = Service(driver_path)
        cls.driver = webdriver.Chrome(service=s)
        cls.bug_name = "test_01"
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(url)
        cls.page = LoginPage(cls.driver)
        cls.doc1 = ReadWrite(file, sheet)
        pass

    @classmethod
    def tearDownClass(cls):
        logger.info('关闭浏览器')
        cls.driver.quit()
        pass

    def setUp(self):
        logger.info("登录禅道")
        data_list = self.doc1.read()
        sleep(2)
        self.page.type_username(data_list[0][0])
        self.page.type_password(data_list[0][1])
        self.page.click_login()
        sleep(2)
        pass

    def tearDown(self):
        logger.info("登出禅道")
        self.page.click_logout()
        pass

    def test_add_bug(self):
        """添加bug"""
        logger.info("执行添加bug测试用例")
        # 点击测试->Bug->提Bug
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        self.driver.find_element(By.XPATH, "//header/div[@id='subHeader']/div[1]/nav[1]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.LINK_TEXT, "提Bug").click()
        # 选择必填项“影响版本”
        self.driver.find_element(By.CLASS_NAME, "search-field").click()
        self.driver.find_element(By.CLASS_NAME, "active-result").click()
        # 输入Bug标题
        self.driver.find_element(By.ID, "title").send_keys(self.bug_name)
        # 滚动条下滑
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        # 点击添加文件
        self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
        sleep(2)
        # 找元素
        # 一级窗口
        dialog = win32gui.FindWindow("#32770", "打开")
        # 二级窗口
        combox_32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        combox = win32gui.FindWindowEx(combox_32, 0, "ComboBox", None)
        # 定义编辑文本框
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        # 定义打开按钮
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")
        # 输入信息
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r"C:\Users\chenchong\Desktop\test.jpg")
        # 点击按钮
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        self.driver.find_element(By.ID, "submit").click()
        sleep(2)
        try:
            self.assertTrue(self.driver.find_element(By.ID, "submit"))
            logger.info('添加bug-----failed')
        except:
            logger.info('添加bug-----passed')
        pass

    def test_bug_resolve(self):
        """解决bug"""
        logger.info("执行解决bug测试用例")
        # 点击测试->Bug->解决Bug
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        self.driver.find_element(By.XPATH, "//header/div[@id='subHeader']/div[1]/nav[1]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[11]/a[2]").click()
        # 选择必填项“解决方案”
        sleep(2)
        self.driver.switch_to.frame("iframe-triggerModal")
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[1]/a[1]").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[1]/div[1]/ul[1]/li[4]").click()
        # 选择必填项“解决版本”
        sleep(1)
        self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/div[1]/div[1]/a[1]").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/div[1]/div[1]/div[1]/ul[1]/li[1]").click()
        sleep(1)
        self.driver.find_element(By.ID, "submit").click()
        sleep(2)
        self.driver.switch_to.default_content()
        try:
            self.assertTrue(self.driver.find_element(By.ID, "submit"))
            logger.info('解决bug-----failed')
        except:
            logger.info('解决bug-----passed')
        pass

    def test_close_bug(self):
        """关闭bug"""
        logger.info("执行关闭bug测试用例")
        # 点击测试->Bug->关闭Bug
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        self.driver.find_element(By.XPATH, "//header/div[@id='subHeader']/div[1]/nav[1]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[11]/a[1]/i[1]").click()
        sleep(2)
        self.driver.switch_to.frame("iframe-triggerModal")
        sleep(1)
        self.driver.find_element(By.ID, "submit").click()
        sleep(1)
        self.driver.switch_to.default_content()
        try:
            self.assertTrue(self.driver.find_element(By.ID, "submit"))
            logger.info('解决bug-----failed')
        except:
            logger.info('解决bug-----passed')
