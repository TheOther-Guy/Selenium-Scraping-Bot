import os
from selenium import webdriver
import selenium
import time
os.environ['PATH'] += r"C:/seleniumdrivers" # this slash should be forward slash else it won't work
driver = webdriver.Chrome()
driver.get('https://pixishoes.com/')

closing_ad = driver.find_element_by_xpath('//*[@id="NewsletterPopup-newsletter-popup"]/div/div/button/svg')
time.sleep(20)
closing_ad.click()

'''shoes_category = driver.find_element_by_class_name("grid__item small--one-half medium-up--one-fifth")
shoes_category.click()'''


