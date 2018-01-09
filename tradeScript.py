from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox(executable_path='/home/vandna/Downloads/geckodriver')
driver = webdriver.Chrome("/home/vandna/Downloads/chromedriver");
driver.get("https://koinex.in/")
#print driver.title
#assert "Koinex" in driver.title
