#Primeira função: cria_mapa 
from base_geral import *
import random
N= u"\u001b[33m▓\u001b[0m"
X= u"\u001b[31m▓\u001b[0m"
A= u"\u001b[37m▓\u001b[0m"
# from funcao_mostrarmapa import *

def mostrar_mapa_comp(mapa_comp,ALFABETO): 
    print("COMPUTADOR- {0}".format(paism)) #Legenda antes de mostrar o mapa do computador

    #Printar letras (parte de cima) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras

    print('\n',end="") 

    #Números laterais e linhas do mapa 

    for i in range (len(mapa_comp)): 
        print(str(i+1)," ",end="") 
        for j in range(len(mapa_comp)): 
            print(mapa_comp[i][j], " ", end="") 
        print(str(i+1)) 

    #Printar letras (parte debaixo) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras

    print('\n',end="") 
    return "" 

def mostrar_mapa_jog(mapa_jogador,ALFABETO): 

    print("JOGADOR-") 
    print("   ",end="")

    for l in ALFABETO: 
        print(l+"  ",end="")

    print('\n',end="") 

    for i in range (len(mapa_jogador)): 
        print(str(i+1)," ",end="") 
        for j in range(len(mapa_jogador)): 
            print(mapa_jogador[i][j], " ", end="") 

        print(str(i+1)) 

    print("   ",end="")

    for l in ALFABETO: 
        print(l+"  ",end="")

    print('\n',end="") 

def cria_mapa(N):
    matriz = []

    for i in range(N):
        linha = []
        for i in range(N):
            linha.append(' ')
        matriz.append(linha)
    return matriz 


#segunda função: posicao_suporta

def posicao_suporta(mapa,blocos,linha,coluna,orientacao): 

    #mapa[linha][coluna] 

            if orientacao == 'v': 
                    for i in range(blocos): 
                        if (linha+i) >= len(mapa): 
                            return False
                        elif mapa[linha+i][coluna] == N: 
                            return False 
                            
            elif  orientacao == 'h': 
                for j in range(blocos): 
                    if (coluna+j) >= len(mapa):
                        return False 
                    
                    elif mapa[linha][coluna+j] == N: 
                         return False 
            return True 

#Terceira função: 

def aloca_navios(mapa, blocos):
    n = len(mapa)
    for blocos_navio in blocos:
        while True:
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            direcao = random.choice(['h', 'v'])

            if posicao_suporta(mapa, blocos_navio, i, j, direcao):

                if direcao == 'h':
                    for z in range(blocos_navio):
                        mapa[i][j + z] = N
                else:
                    for z in range(blocos_navio):
                        mapa[i + z][j] = N
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
            if matriz_quadrada[i][j] == N:
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
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        direcao = random.choice(['h', 'v'])

        while not posicao_suporta(mapa, size_navio, i, j, direcao):
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
            direcao = random.choice(['h', 'v'])

        if direcao == 'h':
            for w in range(j, size_navio + j):
                mapa[i][w] = N
        else:
            for z in range(i, size_navio+ i):
                mapa[z][j] = N
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

#Alocar navios do jogador:

def aloca_navios_jogador(mapa, blocos):
    for blocos_navio in blocos:
        while True:
            j = int(input('Para alocar, informe uma coluna: '))
            i = int(input('Agora, escolha uma linha: '))
            direcao = input('Para qual sentido a embarcação será posicionada? [h/v] ')
            i -= 1
            j -= 1 

            if posicao_suporta(mapa, blocos_navio, i, j, direcao):

                if direcao == 'h':
                    for z in range(blocos_navio):
                        mapa[i][j + z] = N
                else:
                    for z in range(blocos_navio):
                        mapa[i + z][j] = N
            
            print(mostrar_mapa_jog(mapa,ALFABETO))

    return mapa 
