# A Simple Code By ThisMahdi | Telegram : @Thisismahdi

from kavenegar import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time


def buycar():
    driver = webdriver.Firefox()
    # This is a url of Cars for sale
    url = "https://esale.ikco.ir/#!/searchcars?cca=0&csb=1&ccc=0&cpd=0&clt=1"
    site = requests.get(url)
    if site.status_code == 200:
        print("Site is UP")
    else:
        print("Turn Off VPN")
    driver.get(url)
    mytext = driver.find_element_by_xpath('//p[@class="alert alert-danger"]')
    mytextaded = []
    mytextaded.append(mytext.text)
    print(mytextaded)
    if mytextaded[0] == mytextaded[0]:
        print("SMS Not Sent")
    else:
        sendsms()
        print("Sms Sent")


# Code for Kavenegar API SMS System
def sendsms():
    myapi = "Your Key here"
    api = KavenegarAPI(myapi)
    params = {'sender': '1000596446', 'receptor': 'your phone number',
              'message': 'سایت ایرانخودرو باز شده، برو ثبتنام کن'}
    response = api.sms_send(params)


while(true):
    if __name__ == "__main__":
    buycar()
    time.sleep(30000)

# A Simple Code By ThisMahdi | Telegram : @Thisismahdi
