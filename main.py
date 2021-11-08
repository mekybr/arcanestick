import pyautogui
import time
from time import sleep
import keyboard
start_time = time.time()
#pyautogui.PAUSE="3"
pyautogui.FAILSAFE=False
def find_pos():
    sleep(10)
    print(pyautogui.position())
#pyautogui.moveTo(1069,1075)
def start():
    pyautogui.click(1069,1075)
    sleep(3)
    pyautogui.click(1124,92)
    pyautogui.typewrite("hotstar.com/in")
    pyautogui.press("enter")
    pyautogui.hotkey("fn","f11")
    sleep(3)
def navigate_down_initial():
    pyautogui.press(["down","down","down","down","down","down","down","down","down","down","down"])
    pyautogui.moveTo(205,234)
def navigate_up_initial():
    pyautogui.press(["up","up","up","up","up","up","up","up","up","up","up"])
    pyautogui.moveTo(205,234)
def navigate_down():
    numofpressesdown=0
    if numofpressesdown==0:
        navigate_down_initial()
        numofpressesdown+=1
    else:
        pyautogui.moveRel(0,100)
        numofpressesdown+=1
        

    #pyautogui.moveTo(226,530)
    #pyautogui.press(["down","down","down","down","down"])
def navigate_up():
    pyautogui.moveRel(0,-100)
    #pyautogui.moveTo(205,234)
    #pyautogui.press(["up","up","up","up","up"])


def navigate_right(no,gap):
    
    numofpressesright=0
    turns_right=no
    while turns_right != 0 :
        sleep(gap)
        if numofpressesright==4:
            pyautogui.moveTo(1867,287)
            sleep(0.25)
            pyautogui.click(1867,287)
            numofpressesright=0
            pyautogui.moveTo(205,234)
            
        else:
            pyautogui.moveRel(300,0)
            
            numofpressesright+=1
        turns_right+=-1

def navigate_left(no,gap):
    
    numofpressesleft=0
    turns_left=no
    while turns_left != 0 :
        sleep(gap)
        if numofpressesleft==4:
            pyautogui.moveTo(1867,287)
            sleep(0.25)
            pyautogui.click(1867,287)
            numofpressesright=0
            pyautogui.moveTo(205,234)
            
        else:
            pyautogui.moveRel(-300,0)
            
            numofpressesleft+=1
        turns_left+=-1
def press(where):
    pyautogui.click(pyautogui.position())
    if where=="on_tvshow":
        sleep(10)
        pyautogui.click(1793,879)
def pause(where):
    if where=="full_screen":
        pyautogui.click(101,1007)
    if where=="small_screen":
        pass

#find_pos()
'''
start()
navigate_down_initial()
sleep(1)
navigate_up_initial()
sleep(0.5)
navigate_down_initial()
navigate_down()
sleep(1)
navigate_up()
sleep(1)
navigate_right(3,0.25)
navigate_left(2,0.25)
'''
start()
while True:
    if keyboard.is_pressed("w"):
        navigate_up()
    elif keyboard.is_pressed("a"):
        navigate_left(1,0.2)
    elif keyboard.is_pressed("d"):
        navigate_right(1,0.2)
    elif keyboard.is_pressed("s"):
        navigate_down()
    elif keyboard.is_pressed('x'):
        press("on_tvshow")
    elif keyboard.is_pressed('c'):
        pause("fullscreen")
elapsed_time = time.time() - start_time
#if elapsed_time>=6000:
    #quit()
