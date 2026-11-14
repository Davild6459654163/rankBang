#coding:utf-8
#-*-coding:utf-8
#!/usr/bin/env python
#   -- Author: Davild.Bao QQ:839668768 --
# v1.1 基本成型
# v1.2 对无效代码进行清理

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
    for search_keyword in search_keywordList:  #循环读取关键字
        # print search_keyword.decode('unicode_escape')  #unicode解码为中文
        uncode_keyword = search_keyword.decode('unicode_escape')
        for i,proxy in enumerate(open('proxys.txt')):
            #print proxy.strip()
            print '%s|%s|'%(proxy.strip(),uncode_keyword)
            try:
                # baidu_click(u'%s','www.lyw5.com','%s' % (mykeyword,myproxy))
                # baidu_click(mykeyword,'www.lyw5.com',myproxy)
                # pc_baidu(u'五洲旅行','www.82227777.com',proxy.strip())
                mobile_baidu(uncode_keyword,'m.lyw5.com',proxy.strip())
                #print mykeyword,'www.lyw5.com',myproxy
            except Exception as e:
                continue
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

def mobile_baidu(self_keyword,self_url,self_proxy):
	mobileEmulation = {'deviceName': 'Apple iPhone 6'}
	options = webdriver.ChromeOptions()
	# option.add_argument('-incognito')
	options.add_experimental_option('mobileEmulation', mobileEmulation)
	browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
# 未解决代理，和隐身模式开启
	try:
		print u'定点1'
		browser.get("https://m.baidu.com")
	except Exception as e: # 异常进入定点2
		print u'定点2'
	else:
		print u'定点3' ##没有异常执行这块 ，经过定点3
		browser.find_element_by_id("index-kw").send_keys(self_keyword)
		browser.find_element_by_id("index-bn").click()
		print u'定点3.end'
		time.sleep(3)   #搜索完毕有停顿3s
		# 以下为核心代码
		for paggeNub in range(1,6):
			if paggeNub < 2:
				scrollbar(browser) # 提前滚动一下页面，把元素滚动出来
				for rankid in range(1,11):
					domainStrXpath = '''//*[@id="results"]/div[%s]''' % rankid		#提取url的字段string
					domainStr = browser.find_element_by_xpath("%s" % domainStrXpath).text 		#查找url
					domain = self_url
					if domain in domainStr:
						linkXpath = '''//*[@id="results"]/div[%s]/div[1]/a/h3''' % rankid
						browser.find_element_by_xpath("%s" % linkXpath).click()
						time.sleep(180)
					print rankid
				browser.find_element_by_xpath('''//*[@id="page-controller"]''').click()   #第一页找不到会点击，找的到会报错退出
				#找到了后，就无法点击下一页了，直接退出了报错了。是好事情
			else:
				scrollbar(browser) # 提前滚动一下页面，把元素滚动出来
				for rankid in range(1,11):
					domainStrXpath = '''//*[@id="results"]/div[%s]''' % rankid		#提取url的字段string
					domainStr = browser.find_element_by_xpath("%s" % domainStrXpath).text 		#查找url
					domain = self_url
					if domain in domainStr:
						linkXpath = '''//*[@id="results"]/div[%s]/div[1]/a/h3''' % rankid
						browser.find_element_by_xpath("%s" % linkXpath).click()
						time.sleep(180)
					print rankid
				browser.find_element_by_xpath('''//*[@id="page-controller"]/div/div[3]''').click()  #第二页及以后都会点击下一页
			print u"第%s页"%paggeNub

		time.sleep(3) #最终页的停留时间
	finally:
		print u'终点,退出浏览器'
		browser.quit() #不管怎样都会执行这句

if __name__=='__main__':
	for i in range(1,50):
		# 1.获取代理
		# getProxy()
		# 2.读取关键字和ip进行刷词
		main_structure()
		# moblie_baidu_test()
		print i