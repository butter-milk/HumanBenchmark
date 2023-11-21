from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

target = "e6yfngs1"
print("STARTING BROWSER")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(5)
browser.maximize_window()
browser.get("https://humanbenchmark.com/tests/aim")
try:
    browser.find_element(By.CLASS_NAME, "css-1litn2c").click()
except:
      print("No need to accept cookies")

print("Starting test")
sleep(2)
for _ in range(31):
    action = webdriver.common.action_chains.ActionChains(browser)
    action.move_to_element_with_offset(browser.find_element(By.CLASS_NAME, target), 0, 0)
    action.click()
    action.perform()
    
print("End of test")
sleep(10)
browser.quit()