import os
from selenium import webdriver
import selenium
import time
os.environ['PATH'] += r"D:/ALL_data_science/Freecodecamp/Selenium-Scraping-Bot" # this slash should be forward slash else it won't work
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.crunchbase.com/discover/organization.companies')


company_card = driver.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[1]/grid-cell[2]/div/field-formatter/identifier-formatter/a/div/div')
company_card


