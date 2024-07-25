from Funcoes_Atualizando_Locacoes import *

#inicioLoc = janelaInput('Locação de Início', 'Digite a locação a partir da qual se realizará o processo: ')
#fimLoc = janelaInput('Locação Final', 'Digite a locação final do processo: ')

inicioLoc, fimLoc = 'ST1 01C 02B', 'ST1 01A 02D'

# Fazendo tratamento de dados quanto as locações recebidas
inicioLoc = inicioLoc.replace(' ','').upper() # Retirando todos os espaços e deixando tudo em maiúsculo
fimLoc = fimLoc.replace(' ','').upper() # Retirando todos os espaços e deixando tudo em maiúsculo

intervaloLoc = [inicioLoc, fimLoc]
intervaloLoc.sort()

print(intervaloLoc)

# pat.moveTo(1388,1049)
# pat.click()

# pesquisandoLocalDoEstoque(inicioLoc)
# time.sleep(5)
# pesquisandoLocalDoEstoque(fimLoc)