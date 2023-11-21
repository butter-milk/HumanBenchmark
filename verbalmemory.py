from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

buttonStart = "e19owgy710"

print("STARTING BROWSER")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(5)
browser.get("https://humanbenchmark.com/tests/verbal-memory")
try:
    browser.find_element(By.CLASS_NAME, "css-1litn2c").click()
except:
      print("No need to accept cookies")

browser.find_element(By.CLASS_NAME, buttonStart).click()
seenWords = []
STARTTIME = time()
RUNTIME = 30
while time()-STARTTIME < RUNTIME:
    sleep(0.05)
    word = browser.find_element(By.CLASS_NAME, "word").text
    if word in seenWords:
        browser.find_element(By.XPATH, "//button[text()='SEEN']").click() #SEEN button
    else:
        seenWords.append(word)
        browser.find_element(By.XPATH, "//button[text()='NEW']").click() #NEW button
sleep(10)
browser.quit()