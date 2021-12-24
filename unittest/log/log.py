"""
@File:log.py
@DateTime:2021/12/18 21:07
@Author:Ben
@Desc:
"""
import logging
from web_automation.day_07.config.config import log_path

logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_format = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s")
logFile = log_path
fh = logging.FileHandler(logFile, mode='a', encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(log_format)
logger.addHandler(fh)
