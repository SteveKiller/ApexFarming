from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('ManuNotReady.png', region=(0,0,1920,1080), grayscale=True, confidence=0.7) != None:
        click(230, 950)
        time.sleep(0.5)
                
    if pyautogui.locateOnScreen('ManuReady.png', region=(0,0,1920,1080), grayscale=True, confidence=0.7) != None:
         print("Waiting for game")
         time.sleep(5)
    
    
    if pyautogui.locateOnScreen('InGame.png', region=(0,0,1920,1080), grayscale=True, confidence=0.8) != None:
         print("In game waiting")
         keyboard.press_and_release('W')
         time.sleep(0.5)
    
    if pyautogui.locateOnScreen('dead.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
                click(1771, 1040)
                time.sleep(0.5)
                click(1771, 1040)
                
    
    if pyautogui.locateOnScreen('leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
                click(963, 623)
                time.sleep(0.5)
     
    if pyautogui.locateOnScreen('space.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
     keyboard.press_and_release('space')
     
    if pyautogui.locateOnScreen('yes.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
         click(850, 713)
         time.sleep(0.5)
         click(850, 713)
         
