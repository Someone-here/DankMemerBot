from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
em = input("Enter discord email: ")
pas = input("Enter discord password: ")
commands = ["Pls beg", "Pls postmeme", "k", "pls fish", "pls hunt", "pls deposit max"]
url = input("Enter the channel url")

driver = webdriver.Chrome()
driver.get(url)

email = driver.find_element_by_name("email")
email.send_keys(em)
password = driver.find_element_by_name("password")
password.send_keys(pas)
password.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]'))
    )
except:
    driver.quit()
    
while True:
    for i in commands:
            element.send_keys(i + "\n")
            sleep(1)
    sleep(60)
