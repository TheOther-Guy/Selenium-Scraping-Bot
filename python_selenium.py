import os
from selenium import webdriver
import selenium
import time
os.environ['PATH'] += r"D:/ALL_data_science/Freecodecamp/Selenium-Scraping-Bot" # this slash should be forward slash else it won't work
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.crunchbase.com/discover/organization.companies')


company_card = driver.find_element_by_class_name('identifier-label')
company_card.click()


