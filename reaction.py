from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

divReact = "view-go"
divResult = "view-result"
divStart = "view-splash"



print("STARTING BROWSER")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(5)
browser.get("https://humanbenchmark.com/tests/reactiontime")
try:
    browser.find_element(By.CLASS_NAME, "css-1litn2c").click()
except:
      print("No need to accept cookies")
browser.find_element(By.CLASS_NAME, divStart).click()
for i in range(5):
        browser.find_element(By.CLASS_NAME, divReact).click()
        sleep(1)
        if (i!=4):
              browser.find_element(By.CLASS_NAME, divResult).click()
sleep(10)
browser.quit()
