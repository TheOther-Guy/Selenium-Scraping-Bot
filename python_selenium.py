import os
from selenium import webdriver
os.environ['PATH'] += r"C:/seleniumdrivers" # this slash should be forward slash else it won't work
driver = webdriver.Chrome()

