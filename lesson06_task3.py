from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

element = WebDriverWait (driver, 10).until(EC.presence_of_element_located((By.ID, '#text')))

src = driver.find_element(By.CSS_SELECTOR, "img[class='img/award.png']")
txt = src.text
print(txt)