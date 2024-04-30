
# import random

# def posicao_suporta(mapa, blocos, linha, coluna, orientacao): 

#     if orientacao == 'v': 
#         for i in range(blocos): 
#             if (linha+i) >= len(mapa): 
#                 return False
#             elif mapa[linha+i][coluna] == 'N': 
#                 return False 

#     elif  orientacao == 'h': 
#         for j in range(blocos): 
#             if (coluna+j) >= len(mapa):
#                 return False 

#             elif mapa[linha][coluna+j] == 'N': 
#                 return False 
#     return True

# lista_blocos = [1,2,3,5]
# def aloca_navios (mapa, blocos):
#     n = len(mapa)
#     #escolha das variáveis pela máquina:
    
#     for size_navio in blocos:
#         linha = random.randint(0, n-1)
#         coluna = random.randint(0, n-1)
#         orientacao = random.choice(['h', 'v'])

#         while not posicao_suporta(mapa, size_navio, linha, coluna, orientacao):
#             linha = random.randint(0, n-1)
#             coluna = random.randint(0, n-1)
#             orientacao = random.choice(['h', 'v'])

#         if orientacao == 'h':
#             for j in range(coluna, size_navio + coluna):
#                 mapa[linha][j] = 'N'
#         else:
#             for i in range(linha, size_navio+ linha):
#                 mapa[i][coluna] = 'N'
#     return mapa








def cria_mapa(dimensao): 
    lista_final= [] 
    listinha= [] 

    i=0 
    while i < dimensao: 
        listinha.append(' \n') 
        i+=1 

    j=0
    while j < dimensao: 
        lista_final.append(listinha)
        j+=1 

    return lista_final 

mapa_c = cria_mapa(10)
mapa_p = cria_mapa(10)

from base_geral import *

def mostrar_mapa(mapa_cpu,mapa_player,n): 
    print("COMPUTADOR- {0}") 
    
    linha= " " 
    for i in range (n): 
        linha+= " "+ALFABETO+" " 
        esp= " "*2+linha+" "*2