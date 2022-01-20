# 1 - Mascarar IP 
# 2 - Acesso Anonimo
# 3 - Acessar site

import time
import datetime
import webbrowser
import pyautogui

class WatchVideo:
    def __init__(self, tempo_aberto):
        self.tempo_aberto = tempo_aberto

    def watch(self):
        url = 'https://www.youtube.com/watch?v=X89zCSbAPYY'
        chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
        firefox = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
        firefox_privado = 'C:/Program Files/Mozilla Firefox/firefox.exe %s -private'


        actual_time = datetime.datetime.now().strftime("%H:%M:%S")
        set_alarm = datetime.datetime.now() + datetime.timedelta(seconds=3)
        set_alarm = set_alarm.strftime("%H:%M:%S")

        print('Vídeo Abrira: ', set_alarm)

        while (actual_time!=set_alarm):
            print('Hora Atual: ', actual_time)
            actual_time = datetime.datetime.now().strftime("%H:%M:%S")
            time.sleep(1)

        if(actual_time==set_alarm):
            print(set_alarm, " Abrindo navegador...")
            webbrowser.get(firefox_privado).open(url)
            time.sleep(10)
            pyautogui.press('space')
            time.sleep(self.tempo_aberto)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'w')
        
        return 'FIM'

if __name__=='__main__':
    
    tempo_aberto = 200
    vezes = 5

    for i in range(vezes):
        bot = WatchVideo(tempo_aberto)
        res = bot.watch()

    print(res)
