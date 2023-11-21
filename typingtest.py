from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("STARTING BROWSER")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(5)
browser.get("https://humanbenchmark.com/tests/typing")
try:
    browser.find_element(By.CLASS_NAME, "css-1litn2c").click()
except:
    print("No need to accept cookies")
sleep(3)

text = ''.join([el.text if el.text != '' else ' ' for el in browser.find_element(By.CLASS_NAME, "letters").find_elements(By.XPATH, "./*")])
print(text)
browser.find_element(By.CLASS_NAME, "letters").click()
browser.find_element(By.CLASS_NAME, "letters").send_keys(text)
    
sleep(5)
browser.quit()