#Primeira função: cria_mapa 
from base_geral import *
import random



def cria_mapa(N):
    matriz_quadrada = []

    for elemento in range(N):
        linha = []
        for elemento in range(N):
            linha.append(' ')
        matriz_quadrada.append(linha)
    return matriz_quadrada


#segunda função: posicao_suporta

def posicao_suporta(mapa,blocos,linha,coluna,orientacao): 

    #mapa[linha][coluna] 

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

#Terceira função: 

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



#Quarta função: foi_derrotado

#a matriz pode ser de qualquer dimensão;
#cada elemento de raiz quadrada é um caracter;
#a função retorna False caso houver um 'N' como caracter, pois significa que ainda existem navios na matriz;

def foi_derrotado (matriz_quadrada):
    i = 0
    navio = 0
    while i < len(matriz_quadrada):
        j = 0
        while j < len(matriz_quadrada[i]):
            if matriz_quadrada[i][j] == 'N':
                navio +=1
            else:
                navio = navio
            j += 1
        i +=1
    if navio == 0:
        return True
    else:
        return False 
    
import random
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


#função escolher frota: escolher_frota 
def escolher_frota(numero_frota): 
    if numero_frota == 1: 
        mensagem = "Você escolheu a nação Brasil!"
        espaco = "\n"  
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print(mensagem, espaco, mensagem_alocar) 
    
    elif numero_frota == 2: 
        mensagem = "Você escolheu a nação França!" 
        espaco = "\n"
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem,espaco, mensagem_alocar)  
    
    elif numero_frota == 3: 
        mensagem = "Você escolheu a nação Austrália!" 
        espaco = "\n"
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem,espaco, mensagem_alocar)
    
    elif numero_frota == 4: 
        mensagem = "Você escolheu a nação Rússia!" 
        espaco = "\n"
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem, espaco, mensagem_alocar)
    
    elif numero_frota == 5: 
        mensagem = "Você escolheu a nação Japão!" 
        espaco = "\n"
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem, espaco, mensagem_alocar) 
    

#Função lista_blocos 



paism, embarcacoesm = random.choice(list(PAISES.items())) #pais sorteado e lista das embarcações disponíveis para tal país

i=0
for pais in PAISES:
    i += 1
    print("\n")
    print(i, pais)
    for embarcacoes, numero in PAISES[pais].items():
        print("    ", embarcacoes, numero)


def lista_blocos  (embarcacoes,dic_conf):
    quant_emb = list(embarcacoes.values()) #quantas embarcações temos de cada tipo disponível para o país
    nome_embarcacao = list(embarcacoes.keys()) # nomes das embarcações usados para encontrar quantos blocos cada uma ocupa
    lista_b = list(dic_conf.items()) #lista (nome_barco,numero_blocos) do dicionario
    lista_pp = [] #lista que ordena a quantidade de blocos por barco disponível
    lista_nome = [] #lista com nomes repetidos

    indice = 0
    while indice < len(nome_embarcacao):
        indice2 = 0
        while indice2 < quant_emb[indice]:
            lista_nome.append(nome_embarcacao[indice])
            indice2 += 1
        indice += 1


    i = 0
    while i < len(lista_nome):
        barco = lista_nome[i]
        j = 0
        while j < len(lista_b):
            if barco == lista_b[j][0]:
                lista_pp.append(lista_b[j][1])
            j += 1
        i += 1 
        
    return lista_pp


blocos_lista = lista_blocos(embarcacoesm,CONFIGURACAO) #funcao que devolve a lista de blocos disponível por barco disponível

mapa = cria_mapa(10) #precisa mudar a funcao que a variável mapa recebe

mapa_comp = aloca_navios(mapa, blocos_lista) #mapa da máquina 

mapa_jogador= cria_mapa(10)  #Pode ser mudado para mapa(10)


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

#Alocar navios do jogador:

def aloca_navios_jogador(mapa, blocos):
    for blocos_navio in blocos:
        while True:
            coluna = int(input('qual a coluna a ser posiciona? '))
            linha = int(input('qual a linha a ser posiciona? '))
            orientacao = input('qual a orientação a ser posicionada? [h/v] ') 

            if posicao_suporta(mapa, blocos_navio, linha, coluna, orientacao):

                if orientacao == 'h':
                    for i in range(blocos_navio):
                        mapa[linha][coluna + i] = 'N'
                else:
                    for i in range(blocos_navio):
                        mapa[linha + i][coluna] = 'N'
                break
    
    return mapa 
