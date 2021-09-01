from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests 
import time 
from datetime import datetime
from selenium.webdriver.chrome.options import Options

#here fetching url
pageurl = 'https://www.google.co.in/'
browser = webdriver.Chrome('D:/chromedriver.exe')
browser.set_window_size(1920, 1080)
browser.get(pageurl) 

#Passing text in Google search bar field.
Search_input = browser.find_element_by_name("q")
Search_input.send_keys('Jalan Technology Consulting')
print ("Entered text successfully")

#Clicking the Goggle search button.
Google_button = browser.find_element_by_css_selector("input[type='submit'][value='Google Search']")
Google_button.submit()
print ("Google search button has been clicked succesfully.")

time.sleep(10)
#here seaching for JTC website and clicking on that
browser.find_element_by_partial_link_text("JTC: React JS Development Company").click()


