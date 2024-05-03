from funcao_mostrarmapa import * 
from funcoes import * 
from base_geral import *
import random


numero_frota = int(input("Qual o número da nação da sua frota?  "))

lista_paises = list(PAISES.keys())

paisjogador = lista_paises[numero_frota-1]

embarcarcoesjogador = PAISES[paisjogador]

blocos_lista_jogador = lista_blocos(embarcarcoesjogador,CONFIGURACAO)

alocacao_jogador = aloca_navios_jogador(mapa_jogador, blocos_lista_jogador)


#Ataque do computador 

def pc_ataca(mapa_jogador):  
    coluna_num= [0,1,2,3,4,5,6,7,8,9]
    linha_num= [0,1,2,3,4,5,6,7,8,9]
    coluna_ataque_pc = random.choice(list(coluna_num)) 
    linha_ataque_pc = random.choice(list(linha_num)) 

#Não estou sabendo chamar as informações do mapa do jogador

    if mapa_jogador[coluna_ataque_pc][linha_ataque_pc] == 'N': 
        mapa_jogador[coluna_ataque_pc][linha_ataque_pc] = 'X' 

    else: 
        mapa_jogador[coluna_ataque_pc][linha_ataque_pc] = 'A' 
    
    return mostrar_mapa_jog(mapa_jogador,ALFABETO)

print(pc_ataca(mapa_jogador)) 

#Ataque do Jogador 



#Por no main: 
coluna_ataque_jog = int(input("Atacar na coluna:  ")) 
linha_ataque_jog = int(input("Atacar na linha:  ")) 


def jog_ataca(mapa_comp,coluna_ataque_jog, linha_ataque_jog):  

    if mapa_comp[coluna_ataque_jog][linha_ataque_jog] == 'N': 
        'N' == 'X' 

    else: 
        "" == 'A' 

print(jog_ataca(mapa_comp,coluna_ataque_jog, linha_ataque_jog)) 
