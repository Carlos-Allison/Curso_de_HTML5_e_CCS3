
def artilheiros():
    print('''Na Copa do Mundo da Rússia, o prêmio Chuteira de Ouro é dado ao jogador que possui a melhor média de gols na competição.
--------------- VAMOS ANALISAR QUAL JOGADOR RECEBERÁ O PRÊMIO --------------''')
    requisito = ('CLASSIFICATÓRIA', 'OITAVAS', 'QUARTAS', 'SEMI' , 'FINAL')
    matriz = []
    contador = 0
    while True:
        jogador = str(input('Nome do jogador(digite fim para sair): ')).strip().upper()
        if jogador == 'FIM':
            break
        while jogador == '':
            print('Opção inválida. Tente novamente')
            jogador = str(input('Nome do jogador(digite fim para sair): ')).upper()
        rodada = str(input('Rodada [CLASSIFICATÓRIA, OITAVAS, QUARTAS, SEMI, FINAL]: ')).strip().upper()
        while rodada not in requisito:
            print('Opção inválida. Tente novamente')
            rodada = str(input('Rodada [CLASSIFICATÓRIA, OITAVAS, QUARTAS, SEMI, FINAL]: ')).strip().upper()
        numero_gols = int(input('Número de gols: '))
        while numero_gols < 0:
            print('Opção inválida. Tente novamente')
            numero_gols = int(input('Número de gols: ')).strip()
        contador += 1
        for i in range(contador):
            linha = []
            for j in range(1):
                list.append(linha,jogador)
                list.append(linha,rodada)
                list.append(linha,numero_gols)
        matriz.append(linha)    
    return(matriz)

def media_gols():
    matriz = artilheiros()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][1] == 'classificatoria':
                media = matriz[i][2] / 3
            elif matriz[i][1] == 'oitavas':
                media = matriz[i][2] / 4
            elif matriz[i][1] == 'quartas':
                media = matriz[i][2] / 5
            elif matriz[i][1] == 'semi':
                media = matriz[i][2] / 6
            elif matriz[i][1] == 'final':
                media = matriz[i][2] / 7
    print('O jogador {} que jogou até a fase {} e marcou gols {}, tem a média igual {}  '.format(matriz[i][0], matriz[i][1], matriz[i][2], media))

