import random

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

def aloca_navios (mapa, blocos):
    n = len(mapa)
    #escolha das variáveis pela máquina:
    
    for size_navio in blocos:
        linha = random.randint(0, n-1)
        coluna = random.randint(0, n-1)
        orientacao = random.choice(['h', 'v'])

        while not posicao_suporta(mapa, size_navio, linha, coluna, orientacao):
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])

        if orientacao == 'h':
            for j in range(coluna, size_navio + coluna):
                mapa[linha][j] = 'N'
        else:
            for i in range(linha, size_navio+ linha):
                mapa[i][coluna] = 'N'
    return mapa