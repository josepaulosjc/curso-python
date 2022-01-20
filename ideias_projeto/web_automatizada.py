# 1 - Mascarar IP 
# 2 - Acesso Anonimo
# 3 - Acessar site

import time
import datetime
import webbrowser
import pyautogui

url = 'https://www.youtube.com/watch?v=Hzbi4zLI3K4&t=72s'

actual_time = datetime.datetime.now().strftime("%H:%M:%S")
set_alarm = datetime.datetime.now() + datetime.timedelta(seconds=3)
set_alarm = set_alarm.strftime("%H:%M:%S")

while (actual_time!=set_alarm):
    actual_time = datetime.datetime.now().strftime("%H:%M:%S")
    print('Hora Atual: ', actual_time)
    time.sleep(1)

if(actual_time==set_alarm):
    print("You should see you webpage now: ")
    webbrowser.open(url)
    time.sleep(10)
    pyautogui.press('space')
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'w')