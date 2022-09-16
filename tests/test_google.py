from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
wait = WebDriverWait(driver, timeout=2)
driver.implicitly_wait(2)

driver.get('https://google.com./ncr')

driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene')
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys(Keys.ENTER)

def find_element(driver):
    return driver.find_element(By.CSS_SELECTOR, '[name=q]')

wait.until(find_element).send_keys('selene', Keys.ENTER)


wait.until(
    lambda driver: driver.find_element(By.CSS_SELECTOR, '[name=q]')
).send_keys('selene', Keys.ENTER)

wait.until(
    lambda driver: driver.find_element(By.CSS_SELECTOR, '#rso .g h3')
).click