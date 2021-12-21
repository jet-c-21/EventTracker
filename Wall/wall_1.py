# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 12/21/21
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import time

# c = ChromeDriverManager()
# print(c._get_driver_path(c.driver))

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(5)
driver.close()
