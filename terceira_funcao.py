import random
from base_geral import *
from funcoes import * 

paism, embarcacoesm = random.choice(list(PAISES.items())) #pais sorteado e lista das embarcações disponíveis para tal país

blocos_lista = lista_blocos(embarcacoesm,CONFIGURACAO) #funcao que devolve a lista de blocos disponível por barco disponível

mapa = cria_mapa(10) #precisa mudar a funcao que a variável mapa recebe

def posicao_suporta(mapa, blocos, linha, coluna, orientacao): 

    if orientacao == 'v': 
        for i in range(blocos): 
            if (linha+i) >= len(mapa): 
                return False
            elif mapa[linha+i][coluna] == 'N': 
                return False 

    elif  orientacao == 'h': 
        for j in range(blocos): 
            if (coluna+j) >= len(mapa):
                return False 

            elif mapa[linha][coluna+j] == 'N': 
                return False 
    return True

'''def aloca_navios(mapa, blocos):
    n = len(mapa)
    for size_navio in blocos:
        linha = random.randint(0, n - 1)
        coluna = random.randint(0, n - 1)
        orientacao = random.choice(['h', 'v'])

        while not posicao_suporta(mapa, size_navio, linha, coluna, orientacao):
            linha = random.randint(0, n - 1)
            coluna = random.randint(0, n - 1)
            orientacao = random.choice(['h', 'v'])

        if orientacao == 'h':
            for j in range(coluna, coluna + size_navio):
                mapa[linha][j] = 'N'
        else:
            for i in range(linha, linha + size_navio):
                mapa[i][coluna] = 'N'
    return mapa'''

def aloca_navios(mapa, blocos):
    n = len(mapa)
    for blocos_navio in blocos:
        while True:
            linha = random.randint(0, n - 1)
            coluna = random.randint(0, n - 1)
            orientacao = random.choice(['h', 'v'])

            if posicao_suporta(mapa, blocos_navio, linha, coluna, orientacao):

                if orientacao == 'h':
                    for i in range(blocos_navio):
                        mapa[linha][coluna + i] = 'N'
                else:
                    for i in range(blocos_navio):
                        mapa[linha + i][coluna] = 'N'
                break
    
    return mapa

print(aloca_navios(mapa,blocos_lista))