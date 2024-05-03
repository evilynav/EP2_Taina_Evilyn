from base_geral import *
from funcoes import * 

#Mostra mapa atualizado 
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

###### mostrar_mapa_jog ###### 

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