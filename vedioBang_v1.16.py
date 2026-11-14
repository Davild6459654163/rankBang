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

# 1.获取代理并写入到txt文件中


search_keywordList = keywordsConfig.keywordList
# 2.重构结构体，关键词在外部，内部是ip，ip出错跳出来下一个ip，还是用那个关键词
def main_structure():
	pc_baidu()
    # for search_keyword in search_keywordList:  #循环读取关键字
    #     # print search_keyword.decode('unicode_escape')  #unicode解码为中文
    #     uncode_keyword = search_keyword.decode('unicode_escape')
    #     for i,proxy in enumerate(open('proxys.txt')):
    #         #print proxy.strip()
    #         print '%s|%s|'%(proxy.strip(),uncode_keyword)
    #         try:
    #             # baidu_click(u'%s','www.lyw5.com','%s' % (mykeyword,myproxy))
    #             # baidu_click(mykeyword,'www.lyw5.com',myproxy)
    #             # pc_baidu(u'五洲旅行','www.82227777.com',proxy.strip())
    #             pc_baidu(uncode_keyword,'www.lyw5.com',proxy.strip())
    #             #print mykeyword,'www.lyw5.com',myproxy
    #         except Exception as e:
    #             continue
# proxy.txt默认生成的文件格式是dos CR/LF,Unicode-ASCII Escaped
# 需要将keywords文件调整为Unicode字符编码

def stop(num=2):
    time.sleep(random.choice(xrange(160,num)))

def scrollbar(self_driver):
    js='window.scrollTo(0,document.body.scrollHeight/4)'
    js2='window.scrollTo(0,document.body.scrollHeight/2)'
    js3='window.scrollTo(0,document.body.scrollHeight)'
    
    self_driver.execute_script(js)
    time.sleep(1)
    print u'定点7.1'
    self_driver.execute_script(js2)
    time.sleep(1)
    self_driver.execute_script(js3) #拖动滚动条到底部
    time.sleep(1)
    print u'定点7.3'

def action_click(self_driver,self_elem):
	print u'定点4.1'
	ac=ActionChains(self_driver) #每次翻页/刷新都是新对象，所以需要重新初始化
	print u'定点4.2'
	ac.move_to_element(self_elem)
	ac.click(self_elem)
	ac.perform()
	# time.sleep(10)

def pc_baidu():
	option=webdriver.ChromeOptions()
	option.add_argument('-incognito')
	# option.add_argument('--proxy-server=http://%s' % self_proxy)
	browser = webdriver.Chrome(chrome_options=option)

	try:
		print u'定点2 冰箱'
		# browser.get("https://www.toutiao.com/i6624028874122461704/")
		browser.get("http://www.365yg.com/a6625533442136211971/")
		# browser.get("https://www.toutiao.com/i6621025578742972941/")
		# browser.get("https://www.toutiao.com/i6621450110398120456/")
		time.sleep(100)
	except:
		pass #最终页的停留时间

	# try:
	# 	print u'定点3 vivo'
	# 	browser.get("https://www.toutiao.com/i6625533442136211971/")
	# 	browser.get("https://www.toutiao.com/i6621025578742972941/")
	# 	browser.get("https://www.toutiao.com/i6621450110398120456/")
	
	# 	time.sleep(1.5)
	# except:
	# 	pass #最终页的停留时间

	finally:
		print u'终点'
		browser.quit() #不管怎样都会执行这句


if __name__=='__main__':
	for i in range(1,50000):
		# 1.获取代理
		# getProxy()
		# 2.读取关键字和ip进行刷词
		main_structure()
		print i