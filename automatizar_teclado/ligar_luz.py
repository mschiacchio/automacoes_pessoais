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

ligar_luz = pyautogui.locateOnScreen('ligar_luz.png')
pyautogui.click(ligar_luz)
time.sleep(1)

aplicar = pyautogui.locateOnScreen('aplicar.png')
pyautogui.click(aplicar)
time.sleep(2)

processo.terminate()

print('Luzes ligadas! :) ')