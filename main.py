import pyautogui
from PIL import ImageGrab
import datetime
import threading
import time

# SET COORDINATES
XCOOR1 = 680
XCOOR2 = 780


# SET AUTO CLICK FUNCTION
def click(key):
    pyautogui.keyDown(key)
    return


# MANAGE COLLISIONS
def collision(x):
    for i in range(XCOOR1, XCOOR2):
        for j in range(507, 539):
            if x[i, j] < 100:
                click('up')
                return
    return


# COVERT IMAGE
def start():
    im2 = ImageGrab.grab().convert('L')
    data = im2.load()
    collision(data)


# MOVE XCOR2 AFTER 18 sec
def timer():
    global XCOOR2
    global XCOOR1
    second = datetime.datetime.now().second
    if second % 18 == 0:
        time.sleep(5)
        XCOOR2 += 1


# RUN TIMER IN SEPARATED THREAD
time.sleep(3)
while True:
    threading.Thread(target=timer).start()
    start()
