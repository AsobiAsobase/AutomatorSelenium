# -*- encoding=utf8 -*-
__author__ = "jilong.cai"

from airtest.core.api import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.binary_location = r"D:\chrome-win64\chrome.exe"
driver = WebChrome(options=opt,executable_path=r"D:\chrome-win64\chromedriver.exe")

auto_setup(__file__)

driver.get("https://unitygames-int.u3d.cn/")

driver.assert_template(Template(r"tpl1703066106850.png", record_pos=(0.159, -0.017), resolution=(5120, 1440)), "打开游戏中心")
driver.find_element_by_xpath("//img[@src='/public/static/media/user.0dfec411177781cf41aaf283ec1c4aec.svg']").click()
driver.find_element_by_xpath("/html/body/div[2]/div/ul/li/span/div").click()
driver.find_element_by_xpath("//input[@maxlength='11']").send_keys("18859429078")
driver.find_element_by_xpath("//input[@maxlength='6']").send_keys("234567")
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/button").click()
driver.assert_template(Template(r"tpl1703066572810.png", record_pos=(0.218, -0.052), resolution=(5120, 1440)), "登录成功")
driver.find_element_by_xpath("//img[@src='https://gamecenter-cdn.u4ugames.com/images/avatar/Avatar09.webp']").click()
driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[3]/span/div").click()
driver.assert_template(Template(r"tpl1703066636618.png", record_pos=(0.229, -0.052), resolution=(5120, 1440)), "退出登录")
