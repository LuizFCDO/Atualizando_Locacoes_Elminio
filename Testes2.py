intervaloLoc = ['ST103B01A','ST103C03C']
prateleiraMax = '19'
localMax = 'F'

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

for estante in range(letraNumero[estanteIni], letraNumero[estanteFim]+1):
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

print(locacoes)
#[print(i) for i in range(letraNumero[localIni], letraNumero[localMax]+1)]