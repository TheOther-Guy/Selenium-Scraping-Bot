import os
from selenium import webdriver
os.environ['PATH'] += r"C:/seleniumdrivers" # this slash should be forward slash else it won't work
driver = webdriver.Chrome()
driver.get('https://pixishoes.com/')
shoes_category = driver.find_element_by_class_name("grid__item small--one-half medium-up--one-fifth")


