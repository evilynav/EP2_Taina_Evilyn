# from funcoes import * 
# N= u"\u001b[32m▓\u001b[0m"

# numero_frota = int(input("Qual o número da nação da sua frota?  "))

# lista_paises = list(PAISES.keys())

# paisjogador = lista_paises[numero_frota-1]

# embarcarcoesjogador = PAISES[paisjogador]

# blocos_lista_jogador = lista_blocos(embarcarcoesjogador,CONFIGURACAO)

# def aloca_navios_jogador(mapa, blocos):
#     for blocos_navio in blocos:
#         while True:
#             coluna = int(input("Informe a letra:  ")) 
#             linha= int(input("Informe o número:  ")) 
#             orientacao = input("Informe a horientação(h ou v):  ")

#             if posicao_suporta(mapa, blocos_navio, linha, coluna, orientacao):

#                 if orientacao == 'h':
#                     for i in range(blocos_navio):
#                         mapa[linha][coluna + i] = N
#                 else:
#                     for i in range(blocos_navio):
#                         mapa[linha + i][coluna] = N
#                 break
    
#     return mapa 

# print(aloca_navios_jogador(mapa, blocos_lista_jogador)) 