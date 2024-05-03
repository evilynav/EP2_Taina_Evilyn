from funcoes import * 
N= u"\u001b[32m▓\u001b[0m"

paism, embarcacoesm = random.choice(list(PAISES.items())) #pais sorteado e lista das embarcações disponíveis para tal país

blocos_lista = lista_blocos(embarcacoesm,CONFIGURACAO) #funcao que devolve a lista de blocos disponível por barco disponível

mapa = cria_mapa(10) #precisa mudar a funcao que a variável mapa recebe

mapa_comp = aloca_navios(mapa, blocos_lista) #mapa da máquina 

mapa_jogador= cria_mapa(10)  #Pode ser mudado para mapa(10)

 

def aloca_navios_jogador(mapa, blocos):
    for blocos_navio in blocos:
        while True:
            coluna = int(input("Informe a letra:  ")) 
            linha= int(input("Informe o número:  ")) 
            orientacao = input("Informe a horientação(h ou v):  ")

            if posicao_suporta(mapa, blocos_navio, linha, coluna, orientacao):

                if orientacao == 'h':
                    for i in range(blocos_navio):
                        mapa[linha][coluna + i] = N
                else:
                    for i in range(blocos_navio):
                        mapa[linha + i][coluna] = N
                break
    
    return mapa 

print(aloca_navios_jogador(mapa, blocos_lista)) 