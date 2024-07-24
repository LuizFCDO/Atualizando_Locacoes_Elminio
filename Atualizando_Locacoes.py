# Progama feito por Luiz Felipe Carneiro De Oliveira 
# email: luizfelipe.c.d.o@gmail.com      tel.: (64) 99931-8800

from Funcoes_Atualizando_Locacoes import *

################################### Encerrando área de trabalho remota ########################################################

fechandoAreaRemota()

############################## Começando automação ###################################################################

grupo = janelaInput() # Abre janela para coletar o grupo de peças a ser corrigido nas 3 lojas

pat.alert('O código vai começar, não toque no teclado ou no mouse enquanto isso!') # Manda alerta na tela com o texto 

abrindoAreaRemota() # Abre area de trabalho remota, claro kkkk
fechandoApps() # Fecha no máximo 4 coisas abertas na area remota


abrindoCigoELogin() # Abrindo sistema cigo e fazendo o login
time.sleep(5)
