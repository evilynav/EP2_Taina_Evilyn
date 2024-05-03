from base_geral import *
from funcoes import * 
N= u"\u001b[32m▓\u001b[0m"

#Mostra mapa atualizado 


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
