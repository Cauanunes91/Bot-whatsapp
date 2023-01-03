import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['INSIRA O NÚMERO QUE DESEJA MANDAR MSGM']
while len(contatos) >=1:
    pywhatkit.sendwhatmsg(contatos[0],'TESTANDO BOT ', datetime.now().hour,datetime.now().minute+1)
    del contatos[0]
    time.sleep(10)
    keyboard.press_and_release('ctrl + w')
    