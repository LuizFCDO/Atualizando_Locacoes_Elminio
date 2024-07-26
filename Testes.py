from Funcoes_Atualizando_Locacoes import *

conf = True
while conf:
    inicioLoc = janelaInput('Locação de Início', 'Digite a locação a partir da qual se realizará o processo: ') # Recebendo locação inicial do processo
    fimLoc = janelaInput('Locação Final', 'Digite a locação final do processo: ') # Recebendo locação final do processo

    # Fazendo tratamento de dados quanto as locações recebidas
    inicioLoc = inicioLoc.replace(' ','').upper() # Retirando todos os espaços e deixando tudo em maiúsculo
    fimLoc = fimLoc.replace(' ','').upper() # Retirando todos os espaços e deixando tudo em maiúsculo

    if inicioLoc[:5] != fimLoc[:5]: # Garantindo que a locação final e a inicial possuem o mesmo setor e mesma rua(corredor)
        pat.alert('As locações final e inicial devem ser do mesmo setor e da mesma rua!')
    elif len(inicioLoc) < 9 or len(fimLoc) < 9: # Garantindo que locação final e inicial estejam no formato adequado
        pat.alert('Locação de início ou locação final em formato errado, digite novamente!')
    elif not(inicioLoc[:2].isalpha() or fimLoc[:2].isalpha() or inicioLoc[2:5].isnumeric() or fimLoc[2:5].isnumeric() or inicioLoc[5].isalpha() or fimLoc[5].isalpha() or inicioLoc[6:8].isnumeric() or fimLoc[6:8].isnumeric() or inicioLoc[8].isalpha() or fimLoc[8].isalpha()):
        pat.alert('Locação de início ou locação final em formato errado, digite novamente!') # Garantindo que locação final e inicial estejam no formato adequado
    else:
        conf = False

    print(inicioLoc)
    print(fimLoc)