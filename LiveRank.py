from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime
import os


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.livefpl.net/rank")
driver.maximize_window()


Z = driver.find_element(by=By.XPATH, value='//*[@id="s1"]')
Z.send_keys('2027655')


Z1 = driver.find_element(by=By.XPATH, value='//*[@id="form1"]/input[2]')
Z1.click()


Z2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="choose"]'))
)

select = Select(Z2)

select.select_by_visible_text("Free Palestine 🇵🇸✌🏻")

driver.execute_script("window.scrollTo(0, 400);")


screenshot_folder = r'E:\Git&Github\Selenium_Automation\Selenium-Automation\screenshots' 
current_datetime = datetime.datetime.now().strftime("%d-%m_%H-%M")
screenshot_file = f"SS_{current_datetime}.png"

driver.get_screenshot_as_file(f'{screenshot_folder}/{screenshot_file}')


file_path = f'{screenshot_folder}/{screenshot_file}'
os.startfile(file_path)
