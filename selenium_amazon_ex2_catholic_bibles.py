#selenium tutorial 1
# https://www.youtube.com/watch?v=b5jt2bhSeXs
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #gives access to keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

from bs4 import BeautifulSoup
import requests
from csv import writer

#timestamp = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
exec_date = datetime.now().strftime("%m-%d-%Y")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.amazon.com")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("catholic bible") #tells program what to look for
driver.find_element(By.XPATH,"//input[@value='Go']").click()
prices=driver.find_elements(By.XPATH,"//span[contains(@class, 'a-price-whole')]")
names=driver.find_elements(By.XPATH,"//span[contains(@class, 'a-size-medium a-color-base a-text-normal')]")

listing_date = []
listing_name = []
listing_price = []

for name in names:
    #print(name.text) #is printing
    listing_name.append(name.text)
    listing_date.append(exec_date)

for price in prices:
    #print(price.text) #is printing
    listing_price_3 = re.sub('[^0-9,.]', '', price.text)
    listing_price.append(listing_price_3)

final_list=zip(listing_date,listing_name,listing_price)
#creates list object to go in csv

with open('catholic_bibles_amazon'+'_'+exec_date+'.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Listing_Date','Listing_Name','Listing_Price']
    thewriter.writerow(header)
    thewriter.writerows(final_list)
    f.close
#creates csv file

#with open('catholic_bibles_amazon_master.csv', 'a', encoding='utf8', newline='') as f:
#    thewriter = writer(f)
#   thewriter.writerows(final_list)
#    f.close
#supposed to allow user to make a big, dated log, but currently doesn't work

time.sleep(10)
driver.quit()