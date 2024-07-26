from Funcoes_Atualizando_Locacoes import *



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
