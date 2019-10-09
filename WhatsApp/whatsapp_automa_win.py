import urllib.request as url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

# ------------ Checking Internet Connectivity ---------------------

token = -1
try:
    url.urlopen("http://172.217.27.206", timeout = 1)
    print("Internet Available")
    print("-------- Starting Web Whatsapp ---------")
    token = 1
except url.URLError as err:
    token = -1
    print("\nNo Internet :(\n\nPlease check you Internet Connection")

# ------------ Launching WhatsApp ---------------------

if token == 1:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
    driver = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options) # add the path to your chrome webdriver
    driver.set_window_position(0, 0)
    driver.set_window_size(564, 768)
    driver.implicitly_wait
    driver.get('https://web.whatsapp.com')

    # ------------ Message details --------`-------------

    person = input("Enter the Recipient's name: ").strip().split(",")
    message = input("Enter the message: ").strip()
    number_of_messages = int(input("n = ").strip())

    
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._2zCfw')))
    for i in person:
        searchEle = driver.find_element_by_css_selector("._2zCfw")
        searchEle.clear()
        searchEle.send_keys(i)
        searchEle.send_keys(Keys.RETURN)

        meassageEle = driver.find_element_by_css_selector("._3u328")
        meassageEle.clear()
        meassageEle.send_keys((message+"\n")*number_of_messages)
        meassageEle.send_keys(Keys.RETURN)
        time.sleep(1)
        
    print(person)
    # driver.close()

