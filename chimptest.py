from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


print("STARTING BROWSER")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(5)
browser.get("https://humanbenchmark.com/tests/chimp")
try:
    browser.find_element(By.CLASS_NAME, "css-1litn2c").click()
except:
      print("No need to accept cookies")
browser.find_element(By.XPATH, "//button[text()='Start Test']").click()
sleep(1)
no = 1
STARTTIME = time()
RUNTIME = 30
while time()-STARTTIME < RUNTIME:
    try:
        browser.find_element(By.XPATH, f"//div[@data-cellnumber=\"{no}\"]").click()
        no+=1
        
    except:
        browser.find_element(By.XPATH, "//button[text()='Continue']").click()
        no = 1
browser.quit()
        