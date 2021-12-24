"""
@File:runner.py
@DateTime:2021/12/18 16:23
@Author:Ben
@Desc:
"""
import unittest
from BeautifulReport import BeautifulReport

# 加载准备好的测试用例
cases = unittest.defaultTestLoader.discover(start_dir=r"D:\PyCharm\Python_Automation\web_automation\day_07\testcases",
                                            pattern="test*.py")
# 执行测试用例
result = BeautifulReport(cases)
# 生成测试报告
result.report(description="禅道系统的测试报告", filename="SIT测试报告",
              report_dir=r"D:\PyCharm\Python_Automation\web_automation\day_07\report")
