from selenium import webdriver
from selenium.webdriver.chrome.service import Service

##PATH = Service('C:\\BrowserDrivers\\chromedriver.exe')
#driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(executable_path="C:\\BrowserDrivers\\chromedriver")

driver.get("https://www.rcvacademy.com")

