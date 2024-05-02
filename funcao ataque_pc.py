from funcao_mostrarmapa import * 
from funcoes import * 

#Ataque do computador 

def pc_ataca(mapa_jogador):  
    coluna_num= [1,2,3,4,5,6,7,8,9,10]
    linha_num= [1,2,3,4,5,6,7,8,9,10]
    coluna_ataque_pc = random.choice(list(coluna_num)) 
    linha_ataque_pc = random.choice(list(linha_num)) 

#Não estou sabendo chamar as informações do mapa do jogador 

    if mapa_jogador[coluna_ataque_pc][linha_ataque_pc] == 'N': 
        mapa_jogador[coluna_ataque_pc][linha_ataque_pc] = 'X' 

    else: 
        mapa_jogador[coluna_ataque_pc][linha_ataque_pc] = 'A' 
    
    print(mostrar_mapa_jog(mapa_jogador,ALFABETO))
    

    return ""

#Ataque do Jogador 

#Por no main: 
coluna_ataque_jog = int(input("Atacar na coluna:  ")) 
linha_ataque_jog = int(input("Atacar na linha:  ")) 


def jog_ataca(mapa_comp,coluna_ataque_jog, linha_ataque_jog):  

    if mapa_comp[coluna_ataque_jog][linha_ataque_jog] == 'N': 
        'N' == 'X' 

    else: 
        "" == 'A' 


print(pc_ataca(mapa_jogador)) 

print(jog_ataca(mapa_comp,coluna_ataque_jog, linha_ataque_jog)) 
