from companynames import bseNames
from companynames import nseNames
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import json
from selenium.webdriver.common.keys import Keys
import re

start_time = time.process_time()

chrome_options = Options()
#chrome_options.add_extension('extension_1_12_1.crx')
# chrome_options.add_argument('--disk-cache-dir=C:/Users/Kashyap/AppData/Local/Google/Chrome/User Data/Default/Cache')
#chrome_options.add_argument("user-data-dir=C:/Users/Kashyap/AppData/Local/Google/Chrome/User Data/dumdefault")

driver = webdriver.Chrome('chromedriver이 설치된 경로')
# webdriver.PhantomJS('./phantomjs-2.1.1-windows/bin/phantomjs', service_args=['--load-images=no'])

today_date = datetime.date.today().strftime("%Y%m%d")
x = 1
test_number = 1
search = "C($dataRed)"


def testforbse(p, q):
    global test_number
    global x
    print("Test %s" % test_number, "running")
    
    for name in bseNames[p:q]:
        company_name = name
        url_yahoo = "https://in.finance.yahoo.com/q?s=" + company_name
        
        if company_name == "L&amp;TFH.BO":
            url_xpath = '//*[@id="yfs_p43_l"]/span'
        else:
            url_xpath = '//*[@id="quote-header-info"]/div[3]/div/div/span[2]'

        driver.get(url_yahoo)
        pre_title = driver.title
        
        while pre_title == driver.title:
            time.sleep(1)
            break
        
        span_elem = driver.find_element_by_xpath(url_xpath)
        span_cls = span_elem.get_attribute("class")
        
        if search in span_cls:
            span_val = span_elem.get_attribute("innerHTML")
            stock_val = re.sub('<!-- react-text: 38 -->|<!-- /react-text -->','',span_val)
            
        else:
            span_val = span_elem.get_attribute("innerHTML")
            stock_val = re.sub('<!-- react-text: 38 -->|<!-- react-text: 39 -->|<!-- /react-text -->','',span_val)
            
        with open('stocks_info.json', 'r') as fp:
            json_data = json.load(fp)
            json_data['stocks']['today'] = str(today_date)
            json_data['stocks'][company_name] = stock_val

        with open('stocks_info.json', 'w') as fp:
            json.dump(json_data, fp, indent=4)

        print("At t = %s sec " % (time.clock()), company_name, stock_val)
        print("Average time = %s sec" % (time.clock()/x))
        x += 1
    print("Test %s" % test_number, "completed")
    test_number += 1


def testfornse(p, q):
    global test_number
    global x
    print("Test %s" % test_number, "running")
    
    for name in nseNames[p:q]:
        #DLF.NS
        company_name = name
        url_yahoo = "https://in.finance.yahoo.com/q?s=" + company_name
        #//현재 노드로부터 문서상의 모든 노드를 조회
        #*매칭되는 모든 ElementNode
        #[@id id 속성 값이 어쩌구.
        url_xpath = '//*[@id="quote-header-info"]/div[3]/div/div/span[2]'

        driver.get(url_yahoo)
        pre_title = driver.title
        print(pre_title)
        #DLF.NS 224.30 -1.95 -0.86% : DLF LIMITED - Yahoo Finance
        
        while pre_title == driver.title:
            time.sleep(1)
            break
        
        span_elem = driver.find_element_by_xpath(url_xpath)
        #print("span_elem:"+str(span_elem) + "type : " +str(type(span_elem)))
        span_cls = span_elem.get_attribute("class")
        #get_attribute로 받은 span_cls는 srt
        #print("span_cls:"+str(span_cls))

        #span_cls == 'yfi-price-change-red'
        if search in span_cls:
            span_val = span_elem.get_attribute("innerHTML")
            #<!-- react-text: 38 -->-1.95 (-0.86%)<!-- /react-text -->
            #print("span_val:"+str(span_val))
            stock_val = re.sub('<!-- react-text: 38 -->|<!-- /react-text -->','',span_val)
            #-1.95 (-0.86%)
            #print("stock_val:"+str(stock_val))
            #list_span = list(span_val)
            #list_span.remove('(')
            #list_span.remove(')')
            #list_span.remove('%')
            #list_span.insert(0, '-')
            #stock_val = float(''.join(list_span))
            
        else:
            span_val = span_elem.get_attribute("innerHTML")
            #+<!-- react-text: 38 -->-1.95 (-0.86%)<!-- /react-text -->
            #print("span_val:"+str(span_val))
            stock_val = re.sub('<!-- react-text: 38 -->|<!-- react-text: 39 -->|<!-- /react-text -->','',span_val)
            #-1.95 (-0.86%)
            #print("stock_val:"+str(stock_val))

        with open('stocks_info.json', 'r') as fp:
            json_data = json.load(fp)
            json_data['stocks']['today'] = str(today_date)
            json_data['stocks'][company_name] = stock_val

        with open('stocks_info.json', 'w') as fp:
            json.dump(json_data, fp, indent=4)

        print("At t = %s sec " % (time.clock()), company_name, stock_val)
        print("Average time = %s sec" % (time.clock()/x))
        x += 1
    print("Test %s" % test_number, "completed")
    test_number += 1




def end_of_all():
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
