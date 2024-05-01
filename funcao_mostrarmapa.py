from base_geral import ALFABETO 
from main import * 


#Mostra mapa atualizado 
def mostrar_mapa(mapa_comp,ALFABETO): 
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


print(mostrar_mapa(mapa_comp,ALFABETO)) 


