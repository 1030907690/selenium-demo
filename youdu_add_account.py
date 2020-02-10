# -*- coding: utf-8 -*-


from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import platform

'''
有度添加帐号
zhouzhongqing
2020年02月09日12:51:15
'''

if __name__ == '__main__':
    print('start')

    account_list = ['zhouzhongqing','shuruoxuan','qinhao','lipengcheng','tangweijia'
                    ,'zhengdegang','weidong','lihaibo','chuanhao','huguangjian','hehongjun'
                    ,'huangjin','tangyikang','zhangmingxuan','panchenghong','gongcheng'
                    ]
    account_name_list = ['周仲清','舒若旋','秦豪','李鹏程','唐维佳',
                         '郑德刚','韦东','李海波','传浩','胡光健','贺洪君'
                         ,'黄进','唐义康','张铭轩','潘成洪','龚骋'
                         ]

    access_url = 'http://120.132.14.121:7080/userportal/login.html'
    passwd = 'test'
    #驱动程序路径 默认Linux
    executable_path = os.getcwd() + "/driver/chromedriver"

    if "Windows" == platform.system():
        executable_path = os.getcwd() + "/driver/windows/chromedriver.exe"


    if len(account_name_list) == len(account_list):
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

            driver.find_element_by_xpath("//input[@id='userName']").send_keys('administrator')
            driver.find_element_by_xpath("//input[@id='passwd']").send_keys(passwd)
            #登陆提交
            driver.find_element_by_xpath("//button[@class='ydbtn ydbtn-primary next']").click()
            driver.implicitly_wait(10)
            #print(driver.page_source)
            try:
                ##关闭弹窗
                driver.find_element_by_xpath("//*[@id=\"modal-version-3-2\"]/div/div[1]/a").click()
            except Exception as a3:
                print(a3)
            #点击通讯录
            driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
            driver.implicitly_wait(3)
            driver.find_element_by_xpath("//*[@id=\"dept1\"]/div[2]/a").click()

            #新增成员
            driver.find_element_by_xpath('//*[@id="list-btn-user"]/a').click()
            driver.find_element_by_xpath('//*[@id="list-btn-user"]/ul/li[1]/a').click()
            #driver.execute_script("alert(1)")

            for index,item in enumerate(account_list):
                driver.find_element_by_xpath('//*[@id="f_account"]').send_keys(item)
                driver.find_element_by_xpath('//*[@id="f_name"]').send_keys(account_name_list[index])
                driver.find_element_by_xpath('//*[@id="f_pwd"]').send_keys('123456')
                driver.find_element_by_xpath('//*[@id="user_info_edit"]/div[1]/div[2]/button[3]').click()
                time.sleep(2)
                try:
                    close_tips = driver.find_element_by_xpath('//div[@class="box_inner"]/div[3]/button[@class="ydbtn "]')
                    if close_tips:
                       print("tip is not null")
                       close_tips.click()
                       driver.find_element_by_xpath('//*[@id="f_account"]').clear()
                       driver.find_element_by_xpath('//*[@id="f_name"]').clear()
                       driver.find_element_by_xpath('//*[@id="f_pwd"]').clear()
                except Exception as e2:
                    print(e2)
                finally:
                    print()
                time.sleep(5)


            time.sleep(5)
            driver.close()
        except Exception as e:
            print(e)
        finally:
            print()
        print('end')