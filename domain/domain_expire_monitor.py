# -*- coding: utf-8 -*-

'''
zzq
zhouzhongqing
2020年03月11日21:42:38
域名过期监控
'''
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import platform


#驱动程序路径 默认Linux
executable_path = os.getcwd() + "/../driver/chromedriver"

if "Windows" == platform.system():
    executable_path = os.getcwd() + "/../driver/windows/chromedriver.exe"

def edns_monitor():
    '''
    金名网域名过期监控
    :return:
    '''
    access_url = 'http://www.edns.com.cn'
    user_name = ''
    pwd = ''
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get(access_url)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id=\"UserName\"]").send_keys(user_name)
    driver.find_element_by_xpath("//*[@id=\"Password\"]").send_keys(pwd)
    driver.find_element_by_xpath('//*[@id="loginBox"]/button').click()
    driver.implicitly_wait(30)
    #定位到要悬停的元素
    move = driver.find_element_by_xpath('//*[@id="jm-menu"]/div/ul/li[10]/a')
    #对定位到的元素执行悬停操作
    ActionChains(driver).move_to_element(move)#.perform()
    time.sleep(12)
    print('域名')
    driver.find_element_by_xpath('//*[@id="center-list"]/li[1]/ul/li[3]/a').click()

    time.sleep(10)

if __name__ == '__main__':
    print("start")
    edns_monitor()
    print("end")