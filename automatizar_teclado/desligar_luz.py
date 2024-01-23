import pyautogui
import subprocess
import time

processo = subprocess.Popen(['C:\\Program Files (x86)\\PGP631K\\Pichau Gaming P631K.exe'])

time.sleep(2)
config_ilum = pyautogui.locateOnScreen('config_ilum.png')
pyautogui.click(config_ilum)
time.sleep(1)

setinha = pyautogui.locateOnScreen('setinha.png')
pyautogui.click(setinha)
time.sleep(1)

descer = pyautogui.locateOnScreen('descer.png')
pyautogui.click(descer)
time.sleep(0.5)
pyautogui.click(descer)
time.sleep(0.5)
pyautogui.click(descer)
time.sleep(1)

desligar_luz = pyautogui.locateOnScreen('customizar.png')
pyautogui.click(desligar_luz)
time.sleep(2)

aplicar = pyautogui.locateOnScreen('aplicar.png')
pyautogui.click(aplicar)
time.sleep(2)

processo.terminate()

print('Luzes desligadas! :) ')