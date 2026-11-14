#coding:utf-8
#-*-coding:utf-8
#!/usr/bin/env python
#   -- Author: Davild.Bao QQ:839668768 --
# v1.5 添加代理
# v1.6 20170316 重构代码结构
# v1.8 20170316 重构访问百度代码baidu_click()
# v1.9 20170308 1.8遇到严重错误打算重写整个pc_baidu()
# v1.12 20170321 更改点击方式
# v1.13 20170324 多ip点击
# v1.16 20170413 加入循环通过id点击下一页，实现完毕。
# 
# # 代码环境 cygwin、python2.7，安装selenium；selenium的版本和driver的版本要对应，否则无法调取出浏览器
import sys,time
reload(sys)  
sys.setdefaultencoding('utf8')
# ---------------------package start -------------------------
import time,sys,os,codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import keywordsConfig
# ---------------------package end ----------------


mobileEmulation = {'deviceName': 'Apple iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

driver.get('https://m.baidu.com')

time.sleep(3)
driver.close()