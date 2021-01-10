from selenium import webdriver
import keyboard as kb
from time import sleep
from selenium.webdriver.chrome.options import Options
import pyautogui as pt
import sys

#first 4 lines just open chrome
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") 
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://discord.com/app')

#Varaibles and lists
bot_start = False
commands = ['pls beg', 'pls postmeme', 'k', 'pls hunt', 'pls fish', 'pls deposit max']
#to determine when to start bot
while bot_start == False:
    if kb.is_pressed('ctrl'):
        bot_start = True
sleep(1)

#To execute the comands
while True:
    abc = 0
    for command in commands:
        pt.typewrite(command, interval=0.1)
        pt.typewrite('\n')
        sleep(1)
    while abc <= 60:
        sleep(0.01)
        if kb.is_pressed('z'):
            driver.quit()
            sys.exit()
        abc += 0.01
