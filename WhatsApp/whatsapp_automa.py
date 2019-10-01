import urllib.request as url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    driver = webdriver.Chrome('/home/shyam/chromedriver')
    driver.get('https://web.whatsapp.com')

    # ------------ Message details ---------------------

    person = input("Enter the Recipient's name: ").strip().split(",")
    message = input("Enter the message: ").strip()
    number_of_messages = int(input("n = ").strip())

    # message = "Hey guys, let's solve this fun challenge to brush up your mathematical skills.\nAsk doubts if any! Happy Coding! 😀"

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
    # time.sleep(5)
    # driver.close()
