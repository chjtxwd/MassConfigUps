 # -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:23:12 2020

@author: Haijin
"""
def deploy (str):
 from selenium import webdriver
 global browser
 browser = webdriver.Firefox()
 global dnsserver
 dnsserver = str.rsplit('.',1)[0] + '.17'
 browser.get('http://'+str)
 try:
  browser.find_element_by_class_name('modal-header')
 except:
     case1(browser)
 else:
     case2(browser)
 return

def case1 (browser):
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    from time import sleep
    #login
    try:
        a =browser.find_element_by_xpath(".//*[@name='prefLanguage']")
        a.find_element_by_xpath("//option[@value='00000000']").click()
    except:
        print("no language selection, skip")
    browser.find_element_by_name("login_username").send_keys("username")
    browser.find_element_by_name("login_password").send_keys("password")
    browser.find_element_by_name("login_password").send_keys(Keys.ENTER)
    browser.implicitly_wait(30)   
    #set email sender smtp server
    browser.find_element_by_link_text("Administration").click()
    browser.find_element_by_link_text("Notification").click()
    browser.find_element_by_link_text("server").click()
    browser.find_element_by_name("arak_smtpServer").clear()
    browser.find_element_by_name("arak_smtpServer").send_keys("mta.org")
    browser.find_element_by_name("arak_emailSender").clear()
    browser.find_element_by_name("arak_emailSender").send_keys("ups_alarm@auto.com")
    browser.find_element_by_name("submit").click()
    browser.find_element_by_link_text("recipients").click()
    level2 = browser.find_elements_by_link_text("DECAPAC2@dd.net")
    haijinmail = browser.find_elements_by_link_text("haijin.cheng.partner@dd.com")
    if haijinmail != [] :
        print ("haiijn")
        try:
            browser.find_element_by_xpath(".//*[@href='emrep.htm?rcpt=1']").click()
        except:
            browser.find_element_by_xpath(".//*[@href='emrep.htm?rcpt=0']").click()
        try:
            browser.find_element_by_xpath('//input[@value="Delete Recipient"]').click()
        except:
            browser.find_element_by_xpath('//input[@value="Delete"]').click()
        browser.find_element_by_name("submit").click()
        sleep(90)
    if level2 != []:
        print("level2")
        try:
            browser.find_element_by_xpath(".//*[@href='emrep.htm?rcpt=1']").click()
        except:
            browser.find_element_by_xpath(".//*[@href='emrep.htm?rcpt=0']").click()
        try:
            browser.find_element_by_xpath('//input[@value="Delete Recipient"]').click()
        except:
            browser.find_element_by_xpath('//input[@value="Delete"]').click()
            browser.find_element_by_name("submit").click()
            sleep(90)
    browser.find_element_by_link_text("recipients").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("arak_emailTo").clear()
    browser.find_element_by_name("arak_emailTo").send_keys("DECAPAC2@dd.net")
    browser.find_element_by_name("submit").click()
    #start disable all
    print("start disable all")
    browser.find_element_by_link_text("Administration").click()
    browser.find_element_by_link_text("Notification").click()
    browser.find_element_by_link_text("by group").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_xpath('//input[@value="email"]').click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("eventRecipName").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_xpath('//input[@value="disable"]').click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("submit").click()
    browser.implicitly_wait(30)
    #check if mail is enable , if not enable
    browser.find_element_by_link_text("recipients").click()
    browser.find_element_by_link_text("DECAPAC2@dd.net").click()
    selected = browser.find_element_by_name("emailGeneration").is_selected()
    if (selected == False):
        browser.find_element_by_name("emailGeneration").click()
        browser.find_element_by_name("submit").click()
    # set dns server
    browser.find_element_by_link_text("Administration").click()
    browser.find_element_by_link_text("Network").click()
    try:
        browser.find_element_by_link_text("servers").click()
    except:
        browser.find_element_by_link_text("configuration").click()
    browser.find_element_by_name("PrimaryDNSServer").clear()
    browser.find_element_by_name("PrimaryDNSServer").send_keys(dnsserver)
    browser.find_element_by_name("submit").click()
    browser.implicitly_wait(45)
    #enable all   event
    browser.find_element_by_link_text("Administration").click()
    browser.find_element_by_link_text("Notification").click()
    browser.find_element_by_link_text("by group").click()
    browser.find_element_by_name("grpSeverityWarn").click()
    browser.find_element_by_name("grpSeverityInfo").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_xpath('//input[@value="email"]').click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_xpath('//input[@value="?1"]').click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("rec_defaultRepeatIntervalString").send_keys(Keys.BACKSPACE)
    browser.find_element_by_name("rec_defaultRepeatIntervalString").send_keys("12")
    s1 = Select(browser.find_element_by_name('rec_defaultRepeatIntervalUnits'))
    s1.select_by_index(2)
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("submit").click()
    browser.implicitly_wait(45)
    #disable few events
    browser.find_element_by_link_text("by event").click()
    browser.find_element_by_link_text("Power Events").click()
    try:
        browser.find_element_by_xpath("//a[@href='eventdtl.htm?code=0x0102']").click()
        browser.find_element_by_name("i4emailEnable").click()
        browser.find_element_by_name("submit").click()
    except:
            print ("no event 102")
    browser.find_element_by_link_text("Power Events").click()
    try:
        browser.find_element_by_xpath("//a[@href='eventdtl.htm?code=0x0106']").click()
        browser.find_element_by_name("i4emailEnable").click()
        browser.find_element_by_name("submit").click()
    except:
            print("no event 106")
    browser.find_element_by_link_text("Power Events").click()
    browser.find_element_by_xpath("//a[@href='eventdtl.htm?code=0x0107']").click()
    browser.find_element_by_name("i4emailEnable").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_link_text("Power Events").click()
    browser.find_element_by_xpath("//a[@href='eventdtl.htm?code=0x0122']").click()
    browser.find_element_by_name("i4emailEnable").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_link_text("Power Events").click()
    browser.find_element_by_xpath("//a[@href='eventdtl.htm?code=0x0125']").click()
    browser.find_element_by_name("i4emailEnable").click()
    browser.find_element_by_name("submit").click()
    #send test mail
    print("do test")
    browser.find_element_by_link_text("Administration").click()
    browser.find_element_by_link_text("Notification").click()
    browser.find_element_by_link_text("test").click()
    browser.find_element_by_name("submit").click()
    sleep(10)
    browser.close()
    return
def case2(browser):
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    from time import sleep
    browser.find_element_by_xpath(".//*[@name='prefLanguage']/option[2]").click()
    browser.find_element_by_name("login_username").send_keys("apc")
    browser.find_element_by_name("login_password").send_keys("apc")
    browser.find_element_by_name("login_password").send_keys(Keys.ENTER)
    sleep(10)
    #set dnsserver
    print("set dns")
    currenturl = browser.current_url
    needurl = currenturl.rsplit('/',1)[0]
    targeturl = needurl + '/dnscfg.htm'
    browser.get(targeturl)
    browser.find_element_by_name("PrimaryDNSServer").clear()
    browser.find_element_by_name("PrimaryDNSServer").send_keys(dnsserver)
    browser.find_element_by_name("submit").click()
    #config email server
    print("set email server")
    targeturl = needurl + '/emserver.htm'
    browser.get(targeturl)
    browser.find_element_by_name("arak_smtpServer").clear()
    browser.find_element_by_name("arak_smtpServer").send_keys("mta.subsidia.org")
    browser.find_element_by_name("arak_emailSender").clear()
    browser.find_element_by_name("arak_emailSender").send_keys("ups_alarm@auto.com")
    browser.find_element_by_name("submit").click()
    #config Recipients 
    print("set recipients")
    targeturl = needurl + '/emrcpt.htm'
    browser.get(targeturl)
    source = browser.page_source
    level2 = source.find("DECAPAC2@dd.net")
    if level2 == -1 :
        browser.find_element_by_name("submit").click()
    else:
        browser.find_element_by_xpath(".//*[@href='emrep.htm?rcpt=0']").click()
    browser.find_element_by_name("arak_emailTo").clear()
    browser.find_element_by_name("arak_emailTo").send_keys("DECAPAC2@dd.net")
    check = browser.find_element_by_name("emailGeneration").is_selected()
    if(not check):
        browser.find_element_by_name("emailGeneration").click()
    browser.find_element_by_name("submit").click()
    #config event
    print("start config event")
    targeturl = needurl + '/eventgrp.htm'
    browser.get(targeturl)
    browser.find_element_by_name("submit").click()
    browser.find_element_by_id("langEmailRecipients").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("eventRecipName").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_id("langDisable").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("submit").click()
    browser.implicitly_wait(60)
    browser.get(targeturl)
    browser.find_element_by_name("grpSeverityWarn").click()
    browser.find_element_by_name("grpSeverityInfo").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_xpath(".//*[@value='email']").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("eventRecipName").click()
    browser.find_element_by_name("submit").click()
    browser.find_element_by_id("rec_defaultRepeatIntervalString").clear()
    browser.find_element_by_id("rec_defaultRepeatIntervalString").send_keys("12")
    a=Select(browser.find_element_by_id("rec_defaultRepeatIntervalUnits"))
    a.select_by_index(2)
    browser.find_element_by_name("submit").click()
    browser.find_element_by_name("submit").click()
    browser.implicitly_wait(60)
    targeturl = needurl + '/eventind.htm'
    browser.get(targeturl)
    browser.find_element_by_xpath(".//*[@href='eventlst.htm?grp=1&cat=0']").click()
    browser.find_element_by_xpath(".//*[@href='eventdtl.htm?code=0x0102']").click()
    browser.find_element_by_name("i4emailEnable").click()
    browser.find_element_by_name("submit").click()
    try:
        browser.find_element_by_xpath(".//*[@href='eventdtl.htm?code=0x0106']").click()
        browser.find_element_by_name("i4emailEnable").click()
        browser.find_element_by_name("submit").click()
    except:
        print("no 106 event , skip")
    browser.find_element_by_xpath(".//*[@href='eventdtl.htm?code=0x0107']").click()
    browser.find_element_by_name("i4emailEnable").click()
    browser.find_element_by_name("submit").click()
    try:
        browser.find_element_by_xpath(".//*[@href='eventdtl.htm?code=0x0122']").click()
        browser.find_element_by_name("i4emailEnable").click()
        browser.find_element_by_name("submit").click()
    except:
        print("no event 122,skip")
    browser.find_element_by_xpath(".//*[@href='eventdtl.htm?code=0x0125']").click()
    browser.find_element_by_name("i4emailEnable").click()
    browser.find_element_by_name("submit").click()  
    browser.implicitly_wait(60)
    #send test mail
    print("start test")
    targeturl = needurl + '/emtest.htm'
    browser.get(targeturl)
    sleep(30)
    browser.find_element_by_name("submit").click()
    sleep(5)
    browser.close()
    return
text_file = open('G:\\chj\\ups_alarm\\upslist.txt', "r")
list1 = text_file.readlines()
for each in list1:
    try:
        print("  deploy :",each)
        deploy(each)
        print("  ok :",each)
    except Exception as e:
        print ( "  error :",each)
        print(e)
        browser.close()
    continue
