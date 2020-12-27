from selenium import webdriver
import time 
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
browser.get("https://developer.huawei.com/consumer/en/")

signIn = browser.find_element_by_xpath("//*[@id='portal_login']");
time.sleep(3)

signIn.click()
time.sleep(5)
if browser.find_elements_by_css_selector('.button-base-box'):
    print("LOG IN button exists")
time.sleep(2)


browser.close()