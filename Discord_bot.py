import pyautogui as pt
from time import sleep
import pyperclip
import random
import sys
import keyboard as Kb

def copy():
    pt.keyDown("ctrl")
    pt.keyDown("c")
    pt.keyUp("ctrl")
    pt.keyUp("c")

while True:
    if Kb.is_pressed('p'):
        sys.exit()
    sleep(12)
    #pls search execution
    pt.moveTo(400, 700, duration=0.5)
    pt.click()
    pt.typewrite("pls search", interval=0.1)
    pt.typewrite("\n")
    sleep(3)
    #copying a response
    pt.moveTo(394, 628, duration=0.1)
    pt.doubleClick()
    copy()
    #giving the response
    pt.moveTo(400, 700, duration=0.1)
    pt.click()
    message = pyperclip.paste()
    if message == "christmas": 
        message = "christmas tree"
    elif message == "santa":
        message = "santa claus"
    pt.typewrite(message, interval=0.1)
    pt.typewrite("\n")
    #wait
    sleep(18)
    #pls beg execution
    pt.moveTo(400, 700, duration=0.1)
    pt.click()
    pt.typewrite("pls beg", interval=0.1)
    pt.typewrite("\n")
    #pls coins execution
    pt.moveTo(400, 700, duration=0.1)
    pt.click()
    pt.typewrite("pls coins", interval=0.1)
    pt.typewrite("\n")
    #storing the value of coins
    sleep(2.5)
    pt.moveTo(451, 549, duration=0.1)
    pt.doubleClick()
    copy()
    coins = pyperclip.paste()
    #removing commas from the obtained values
    try:
        coins = int(coins.replace(",", ''))
         #Gambling the money if it is more than 2000 coins
        if coins > 2000:
            pt.moveTo(400, 700, duration=0.1)
            pt.click()
            pt.typewrite("pls roll 1000", interval=0.1)
            pt.typewrite("\n")
        #Depositing the excess money in bank.
        pt.moveTo(400, 700, duration=0.5)
        pt.click()
        pt.typewrite("pls deposit " + 'max', interval=0.1)
        pt.typewrite("\n")  
    except:
        print('invalid turn')
                


