from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
import time
import argparse
from selenium.webdriver.common.proxy import Proxy, ProxyType
from numpy import random
from time import sleep
import random
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import pyautogui
from selenium.webdriver.support.ui import Select
import pyshorteners
from datetime import datetime
import os
import urllib.request
import requests
from termcolor import colored
from colorama import init
import threading
from random import randint
import json
import random

''' ask user to input the instagram post url '''
link = input("Enter Instagram Image URL: ")
img = input("enter scrape counr need to scrape")

list_user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0']
ua = UserAgent()
#userAgent = ua.random
userAgent = random.choice(list_user_agents)
print(userAgent)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = Options()
options.add_argument("--lang=en")
options.user_data_dir = "c:\\temp\\profile"
options.add_argument('--user-data-dir=c:\\temp\\profile22000')
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument(f'user-agent={userAgent}')

options.add_argument("--lang=fr")
options.add_argument("--lang=fr-ca")
options.add_argument("--lang=aus")

driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")     

#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
time.sleep(1)




driver.get(link)
time.sleep(10)
linkscscs = input("Enter Instagram Image URL: ")
soup = BeautifulSoup(driver.page_source, 'lxml')



print(img)

for x in range(1,int(img)):
    try:
        imgsave = driver.find_element_by_xpath('(//div[@class="buofh1pr hv4rvrfc"]/descendant::span[1])['+str(x)+']').text
        img_url = imgsave
        
        file = open("text.txt", "a+",encoding='utf-8') 
        file.write(img_url) 
        file.write("\n") 
        file.close() 
        driver.execute_script("window.scrollTo(0, 500000000000)")
        print(img_url)
        time.sleep(0.4)
    except Exception:
        driver.execute_script("window.scrollTo(0, 500000000000)")
        print("exeption")
        time.sleep(5)

print('success')