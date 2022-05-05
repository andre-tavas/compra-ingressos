from selenium import webdriver
import pyautogui
import pyperclip
import time
from datetime import datetime

# INSIRA A HORA DO INICIO DAS VENDAS
hora = '10:42'
# HORARIO PARA ALERTA
alert = '10:41'
# INSIRA O LINK QUE SE INICIARA AS VENDAS
link = 'https://www.sympla.com.br/evento/festival-planeta-brasil-24-e-25-de-setembro-2022/1421795'

def reserva_ingressos(t, link):
  '''
  Abre o site e reserva os ingressos
  '''
  # Abre nova aba
  pyautogui.hotkey('ctrl','t')
  time.sleep(1)
    
  # Entra no site da plataforma
  pyperclip.copy(link)
  pyautogui.hotkey('ctrl', 'v')
  pyautogui.press('enter')
  time.sleep(5)

  # Rola a tela para ficar na altura correta dos cliques
  pyautogui.scroll(-770)
    
  time.sleep(2)
    
  if t == 1:
    pyautogui.click(1594,167)  # INGRESSO 1
    pyautogui.click(1594,284)  # INGRESSO 2
    pyautogui.click(1594,401)  # INGRESSO 3
    pyautogui.click(1594,518)  # INGRESSO 4
    pyautogui.click(1594,611)  # INGRESSO 5

    pyautogui.click(1470,815)

# Abre pop up alertando que o inicio ocorrerá em breve e deve-se para de usar o PC
aux = True
while aux:
    hour = int(datetime.today().strftime('%H:%M')[:2])
    minut = int(datetime.today().strftime('%H:%M')[3:])
    horario = str(hour) + ':' + str(minut)
    if horario == alert:
        print(horario)
        pyautogui.alert('falta 1 min')
        aux = False

# Reserva os ingressos e aparece pop up para finalizar a compra manualmente
aux = True
while aux:
        if datetime.today().strftime('%H:%M') == hora:
            reserva_ingressos(1,link)
            pyautogui.alert("concluído")
            aux = False
