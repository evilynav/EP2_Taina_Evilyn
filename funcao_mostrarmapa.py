from base_geral import *
from funcoes import * 

paism, embarcacoesm = random.choice(list(PAISES.items())) #pais sorteado e lista das embarcações disponíveis para tal país

blocos_lista = lista_blocos(embarcacoesm,CONFIGURACAO) #funcao que devolve a lista de blocos disponível por barco disponível

mapa = cria_mapa(10) #precisa mudar a funcao que a variável mapa recebe

mapa_comp = aloca_navios(mapa, blocos_lista) #mapa da máquina 

mapa_jogador= cria_mapa(10)  #Pode ser mudado para mapa(10)


#Função mostrar_mapa_comp (PARA O COMPUTADOR) e Função mostrar_mapa_jog (PARA O JOGADOR) 

#Mostra mapa atualizado 
def mostrar_mapa_comp(mapa_comp,ALFABETO): 
    print("COMPUTADOR- {0}".format(paism)) #Legenda antes de mostrar o mapa do computador

    #Printar letras (parte de cima) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras
        if letra == "J": 
            break 
    print('\n',end="") 

    #Números laterais e linhas do mapa 

    for i in range (len(mapa_comp)): 
        print(str(i+1)," ",end="") 
        for j in range(len(mapa_comp)): 
            print(mapa_comp[i][j], " ", end="") 
        print(str(i+1)) 

    #Printar letras (parte de cima) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras
        if letra == "J": 
            break 
    print('\n',end="") 


print(mostrar_mapa_comp(mapa_comp,ALFABETO)) #Nós não vamos printar na tela a posição dos navios do computador, será return. 

###### mostrar_mapa_jog ###### 

def mostrar_mapa_jog(mapa_jogador,ALFABETO): 
    print("JOGADOR-") #Legenda antes de mostrar o mapa do jogador

    #Printar letras (parte de cima) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras
        if letra == "J": 
            break 
    print('\n',end="") 

    #Números laterais e linhas do mapa 

    for i in range (len(mapa_jogador)): 
        print(str(i+1)," ",end="") 
        for j in range(len(mapa_jogador)): 
            print(mapa_jogador[i][j], " ", end="") 
        print(str(i+1)) 

    #Printar letras (parte de cima) 

    print("   ",end="") #Espaçamento inicial 
    for letra in ALFABETO: 
        print(letra+"  ",end="") #determino o espaçamento entre as letras
        if letra == "J": 
            break 
    print('\n',end="") 

print(mostrar_mapa_jog(mapa_jogador,ALFABETO)) 