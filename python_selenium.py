import os
from selenium import webdriver
import selenium
import time
os.environ['PATH'] += r"D:/ALL_data_science/Freecodecamp/Selenium-Scraping-Bot" # this slash should be forward slash else it won't work
driver = webdriver.Chrome()
driver.get('https://pixishoes.com/')

time.sleep(10)
closing_ad = driver.find_element_by_css_selector('#shopify-section-16066484874a6d6f11 > div > div.grid.grid--uniform > div:nth-child(1)').click()

'''time.sleep(20)
closing_ad.click()'''

'''shoes_category = driver.find_element_by_class_name("grid__item small--one-half medium-up--one-fifth")
shoes_category.click()'''


