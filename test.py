#coding = utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver1 = webdriver.Edge()
print(driver.name)
print(driver1.name)

driver.close()

driver1.close()