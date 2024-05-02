# import time 
# from base_geral import *
# import random
# from funcoes import *

# print("=================================") 
# print("Bem-vindo ao INSPER-Batalha Naval!!") 
# print("=================================") 

# time.sleep(0.5)

# print("Iniciando o jogo!") 

# #Trazer a função da Evilyn 

# time.sleep(0.5)

# paism, embarcacoesm = random.choice(list(PAISES.items())) #pais sorteado e lista das embarcações disponíveis para tal país

# blocos_lista = lista_blocos(embarcacoesm,CONFIGURACAO) #funcao que devolve a lista de blocos disponível por barco disponível

# mapa = cria_mapa(10) #precisa mudar a funcao que a variável mapa recebe

# mapa_comp = aloca_navios(mapa, blocos_lista) #mapa da máquina

# print("O computador está alocando os navios de guerra do país {0}...". format(paism)) 
# print("\n")
# print("Computador já está em posição de batalha!") 
# print("\n")

# i=0
# for pais in PAISES:
#     i += 1
#     print("\n")
#     print(i, pais)
#     for embarcacoes, numero in PAISES[pais].items():
#         print("    ", embarcacoes, numero)


# numero_frota = int(input("Qual o número da nação da sua frota?  ")) 
# print(escolher_frota(numero_frota)) 

# print(mapa_comp)



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
