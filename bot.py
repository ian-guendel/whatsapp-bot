import pywhatkit as kit
import time
import datetime
import random
import pyautogui as pg
import time
import keyboard as k
# To schedule messages
# kit.sendwhatmsg('+50688138143',"Bot message")


print('Starting to send the message...')
# To send instant messages
try:
    kit.sendwhatmsg_instantly('+50688138143',"Guapa",9,True,1)
    print('message send!')

except Exception as ex:
    print(ex)
