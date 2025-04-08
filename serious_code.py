import pyautogui
import time

pyautogui.PAUSE = 1

# time.sleep(5)

# print(pyautogui.position())

with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("opera")
pyautogui.press('enter')
time.sleep(3)

pyautogui.write("youtube.com")
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=481, y=142)
pyautogui.write("Rick Astley - Never Gonna Give You Up (Official Music Video)")
pyautogui.press('enter')
time.sleep(3)


pyautogui.click(x=541, y=703)
