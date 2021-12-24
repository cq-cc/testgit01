"""
@File:config.py.py
@DateTime:2021/12/18 20:07
@Author:Ben
@Desc:
"""
import os

# 获取当前文件所在绝对路径
print(os.getcwd())
print(os.path.dirname(__file__))
driver_path = f"{os.path.dirname(os.path.dirname(__file__))}/driver/chromedriver.exe"
url = "http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html"
file = r"D:\PyCharm\Python_Automation\web_automation\day_07\data\testdata.xlsx"
sheet = "login"
log_path = r"D:\PyCharm\Python_Automation\web_automation\day_07\log\log.txt"
