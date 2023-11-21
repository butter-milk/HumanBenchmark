from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

buttonStart = "e19owgy710"

print("STARTING BROWSER")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(5)
browser.get("https://humanbenchmark.com/tests/number-memory")
try:
    browser.find_element(By.CLASS_NAME, "css-1litn2c").click()
except:
      print("No need to accept cookies")

browser.find_element(By.CLASS_NAME, buttonStart).click()
seenWords = []
STARTTIME = time()
RUNTIME = 120
round=0
while time()-STARTTIME < RUNTIME:
    number = browser.find_element(By.CLASS_NAME, "big-number").text
    print(number)
    sleep(3+round)

    browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(number)
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
    browser.find_element(By.XPATH, "//button[text()='NEXT']").click()
    round+=1
browser.quit()