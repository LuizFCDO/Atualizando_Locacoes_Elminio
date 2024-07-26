# Progama feito por Luiz Felipe Carneiro De Oliveira 
# email: luizfelipe.c.d.o@gmail.com      tel.: (64) 99931-8800

from Funcoes_Atualizando_Locacoes import *

################################### Encerrando área de trabalho remota ########################################################

fechandoAreaRemota()

############################## Recebendo dados do usuário ###################################################################

conf = True
while conf: # Looping para input das locações de início e final
    while conf: # Looping para imput da locação de início
        inicioLoc = janelaInput('Locação de Início', 'Digite a locação a partir da qual se realizará o processo: ') # Recebendo locação inicial do processo
        
        # Fazendo tratamento de dados quanto as locações recebidas
        inicioLoc = inicioLoc.replace(' ','').upper() # Retirando todos os espaços e deixando tudo em maiúsculo

        if locCorreta(inicioLoc): # Garantindo que a locação de início esteja no formato adequado
            continue
        conf = False
    
    conf = True
    while conf: # Looping para imput da locação de início
        fimLoc = janelaInput('Locação Final', 'Digite a locação final do processo: ') # Recebendo locação final do processo

        # Fazendo tratamento de dados quanto as locações recebidas
        fimLoc = fimLoc.replace(' ','').upper() # Retirando todos os espaços e deixando tudo em maiúsculo

        if locCorreta(fimLoc): # Garantindo que a locação final esteja no formato adequado
            continue
        conf = False

    conf =  True
    if inicioLoc[:5] != fimLoc[:5]: # Garantindo que a locação final e a inicial possuem o mesmo setor e mesma rua(corredor)
        pat.alert('As locações final e inicial devem ser do mesmo setor e da mesma rua!')
    else:
        conf = False

intervaloLoc = [inicioLoc, fimLoc] # Garantindo que a locação inicial e final estejam na ordem certa
intervaloLoc.sort()

conf = True
while conf: # Looping para input do maior valor de andar(prateleira) da operação
    prateleiraMax = janelaInput('Maior Andar', 'Qual é o andar(prateleira) de maior número entre todos os andares que terão algum apartamento passando pela operação? ')

    # Fazendo tratamento de dados quanto as locações recebidas
    prateleiraMax = prateleiraMax.strip() # Retirando todos os espaços

    if prateleiraMax.isalpha(): # Confirmando que não é um valor vazio e que é um número e não uma letra
        pat.alert('O valor de prateleira deve ser numérico!')
    elif prateleiraMax == '':
        pat.alert('O valor de prateleira não deve ser vazio!')
    else:
        conf = False

conf = True
while conf: # Looping para input do maior valor de apartamento(local) da operação
    localMax = janelaInput('Última Letra de Apartamento','Qual é o apartamento(local) com a última letra do alfabeto entre todos os que passarão pela operação? ')
    
    # Fazendo tratamento de dados quanto as locações recebidas
    localMax = localMax.strip().upper() # Retirando todos os espaços

    if localMax.isnumeric(): # Confirmando que não é um valor vazio e que é uma letra e não um número
        pat.alert('O valor de local deve ser alfabético!')
    elif localMax == '':
        pat.alert('O valor de local não deve ser vazio!')
    else:
        conf = False


########################################### Criando Lista de Locações ##############################################################

letraNumero = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, # Dicionário correspondendo cada letra a um número
               'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
numeroLetra = {letraNumero[chave]:chave for chave in letraNumero} # Dicionário correspondendo cada número a uma letra
numeroNumero = {num:'0'+str(num) for num in range(0,10)} # Dicionário para passar números com um único algarismo para strings iniciadas por '0'

locacoes = [] # A lista contendo todas as locações a serem atualizadas
setor = intervaloLoc[0][:3] # Armazenando o setor das locações
corredor = intervaloLoc[0][3:5] # Armazenando o corredor(rua) das locações
estanteIni = intervaloLoc[0][5] # Armazenando a estante(edifício) da locação inicial
estanteFim = intervaloLoc[1][5] # Armazenando a estante(edifício) da locação final
prateleiraIni = intervaloLoc[0][6:8] # Armazenando a prateleira(andar) da locação inicial
prateleiraFim = intervaloLoc[1][6:8] # Armazenando a prateleira(andar) da locação final
localIni = intervaloLoc[0][8] # Armazenando o local(apartamento) da locação inicial 
localFim = intervaloLoc[1][8] # Armazenando o local(apartamento) da locação final

for estante in range(letraNumero[estanteIni], letraNumero[estanteFim]+1): # Criando lista com todas as locações desde locação inicial até locação final
    if estante == letraNumero[estanteFim]:
        prateleiraMax = prateleiraFim

    for prateleira in range(int(prateleiraIni), int(prateleiraMax)+1):
        if prateleira == int(prateleiraFim) and estante == letraNumero[estanteFim]:
            localMax = localFim

        for local in range(letraNumero[localIni], letraNumero[localMax]+1):
            if prateleira in range(0,10):
                locacoes.append(setor + ' ' + corredor + numeroLetra[estante] + ' ' + numeroNumero[prateleira] + numeroLetra[local])
            else:
                locacoes.append(setor + ' ' + corredor + numeroLetra[estante] + ' ' + str(prateleira) + numeroLetra[local])
        
        localIni = 'A'
    prateleiraIni = 1

########################################### Iniciando Automação ###################################################################

pat.alert('O código vai começar, não toque no teclado ou no mouse enquanto isso!') # Manda alerta na tela com o texto 

abrindoAreaRemota() # Abre area de trabalho remota, claro kkkk
fechandoApps() # Fecha no máximo 4 coisas abertas na area remota


abrindoCigoELogin() # Abrindo sistema cigo e fazendo o login
time.sleep(5)

abrindoLocalDoEstoque() # Abrindo Local do Estoque no sistema

for loc in locacoes: # Atualizando cada locação da lista de locações
    pesquisandoLocalDoEstoque(loc.replace(' ','%'))
    time.sleep(1)
    atualizandoLocacao(loc)
    time.sleep(1)

pat.alert('Fim da operação!') # Indicando o fim da operação