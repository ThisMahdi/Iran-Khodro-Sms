# A Simple Code By ThisMahdi | Telegram : @Thisismahdi

from kavenegar import *
from selenium import webdriver
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
    try:
        nosale = driver.find_element_by_xpath('//p[@id="noItemFound"]')
        if nosale.text == "هیچ برنامه فروشی متناسب با درخواست شما موجود نمیباشد":
            print("No schedule sale on site :(")
    except:
            sendsms()
            print("Sms sent!")


# Code for Kavenegar API SMS System
def sendsms():
    myapi = "Your Key here"
    api = KavenegarAPI(myapi)
    params = {'sender': '1000596446', 'receptor': 'your phone number',
              'message': 'سایت ایرانخودرو باز شده، برو ثبتنام کن'}
    response = api.sms_send(params)


if __name__ == "__main__":
    while True:
    buycar()
    time.sleep(30000)

# A Simple Code By ThisMahdi | Telegram : @Thisismahdi
