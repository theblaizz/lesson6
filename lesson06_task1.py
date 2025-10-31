from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element_by_xpath('//button[contains(@class, "btn btn-primary")]')
                                      
ajax = driver.find_element(By.CSS_SELECTOR, "a[class='bg-success']")
txt = ajax.text
print(txt)