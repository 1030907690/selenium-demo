# -*- coding: utf-8 -*-


from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


'''
有度添加帐号
zhouzhongqing
2020年02月09日12:51:15
'''

if __name__ == '__main__':
    print('start')
    access_url = 'https://www.baidu.com/'
    executable_path = os.getcwd() + "/driver/chromedriver"

    try:
        #driver = webdriver.PhantomJS(executable_path=os.getcwd()+"/driver/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
        driver = webdriver.Chrome(executable_path=executable_path)
        driver.get(access_url)
        driver.implicitly_wait(30)
        '''
        测试
        search_input = driver.find_element_by_xpath("//input[@id='kw']")
        search_input.click()
        search_input.send_keys("test")
        driver.find_element_by_xpath("//input[@class=\"bg s_btn\"]").click()
        '''

        print(driver.page_source)
    except Exception as e:
        print(e)
    finally:
        print()
    print('end')