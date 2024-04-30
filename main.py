import time 
from base_geral import * 
from funcoes import *

print("=================================") 
print("Bem-vindo ao INSPER-Batalha Naval!!") 
print("=================================") 

time.sleep(0.5)

print("Iniciando o jogo!") 

mapa_cpu= (cria_mapa(10)) 
mapa_player= (cria_mapa(10)) 

#Trazer a função da Evilyn 

time.sleep(0.5)

#print("O computador está alocando os navios de guerra do país {0}". format()) 
#print("\n")
#print("Computador já está em posição de batalha") 
print(PAISES)
print("Agora é a sua vez de alocar seus navios de guerra")  

numero_frota = int(input("Qual o número da nação da sua frota?  ")) 
print(escolher_frota(numero_frota)) 




