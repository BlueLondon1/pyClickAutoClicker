from pynput.keyboard import Key, Controller
import time

keyboard = Controller() #Create the controller

time.sleep(2)
keyboard.press('Coucou tu veux voir ma bite')
keyboard.release('Coucou tu veux voir ma bite')