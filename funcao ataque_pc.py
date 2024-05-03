from funcao_mostrarmapa import * 
from funcoes import * 
from base_geral import *
import random

N= u"\u001b[32m▓\u001b[0m"

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

    if mapa_jogador[coluna_ataque_pc][linha_ataque_pc] == N: 
        mapa_jogador[coluna_ataque_pc][linha_ataque_pc] = u"\u001b[31m▓\u001b[0m"


    else: 
        mapa_jogador[coluna_ataque_pc][linha_ataque_pc] = u"\u001b[37m▓\u001b[0m"
 
    
    return mostrar_mapa_jog(mapa_jogador,ALFABETO)

print(pc_ataca(mapa_jogador)) 

#Ataque do Jogador 

coluna_ataque_jog = int(input("Atacar na coluna:  ")) 
linha_ataque_jog = int(input("Atacar na linha:  ")) 



def jog_ataca(mapa_comp,coluna_ataque_jog, linha_ataque_jog):

    if mapa_comp[coluna_ataque_jog][linha_ataque_jog] == N: 
        mapa_comp[coluna_ataque_jog][linha_ataque_jog] =  'X'

    else: 
        mapa_comp[coluna_ataque_jog][linha_ataque_jog] = 'A' 

print(jog_ataca(mapa_comp,coluna_ataque_jog, linha_ataque_jog)) 
