from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://fabrykatestow.pl')
driver.close()