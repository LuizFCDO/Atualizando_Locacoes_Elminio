import pyautogui as pat
import time
from tkinter import Tk, Button # biblioteca para janela de comunicação
from tkinter import simpledialog # biblioteca para janela de comunicação que recebe informação
from os import kill, path, remove # biblioteca para comandos do sistema
import psutil as ps # biblioteca para processos do sistema
import signal # biblioteca para encerrar processos
import pandas as pd

from PosicoesEmpresa import cord # para importar as posições de ponteiro no computador da empresa
#from PosicoesParticular import cord # para importar as posições de ponteiro no computador particular

def pidAreaRemota():
    for proc in ps.process_iter(): # Armazenando pid da área de trabalho remota no pidArea
        info = proc.as_dict(attrs=['pid', 'name'])
        if info['name'] == 'mstsc.exe':
            pidArea = int(info['pid'])
            return pidArea
    return 0

def finalizar_processo(pid): # Função para encerrar processos com base no pid
    kill(pid, signal.SIGTERM)

def fechandoAreaRemota():
    pidArea = pidAreaRemota() # Obtendo o pid da atea de trabalho temota e armazenando em pidArea
    if(pidArea != 0): # Encerrando área de trabalho remota
        finalizar_processo(pidArea)

def janelaInput():
    janela = Tk()   
    janela.title('Janela de entrada')
    janela.geometry('350x200')
    grupo = simpledialog.askstring("Grupo a ser verificado", "Digite o código do grupo de peças a ser verificado:", parent=janela)
    janela.destroy()
    janela.mainloop()
    return grupo

pat.PAUSE = 0.5
pat.MINIMUM_DURATION = 0.25

dataParaSalvamento = time.strftime("%d %m %Y", time.localtime())

empr = {
    'elm' : 'ELMINIO',
    'soc' : 'SOCORRO',
    'wag' : 'WAGNER'
}

def abrindoAreaRemota():
    # Abrindo a área de trabalho remota
    pat.press('win', interval=1)
    pat.write('conex~ao de ´area de trabalho',interval=0.2)
    pat.press('enter', presses=2, interval=1)
    time.sleep(10)

def fechandoApps():
    # Fechando possíveis janelas abertas na área remota
    pat.keyDown('alt') # Equivalente a pat.hotkey('alt', 'f4')
    pat.press('f4', presses=4, interval=0.2)
    pat.keyUp('alt')
    pat.press('esc')

def abrindoCigoELogin():
    time.sleep(1)  
    pat.moveTo(cord['cigo atalho'])
    pat.click(clicks=2)
    time.sleep(8)
    pat.write("21", interval=0.3)
    pat.press('tab')
    pat.write("k123d", interval=0.3)
    pat.press('enter')