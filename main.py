import time 
from base_geral import *
import random
from funcao_mostrarmapa import * #Temporário, enquanto não ponho ele em funcoes 
N= u"\u001b[32m▓\u001b[0m"


print("           ====================================")
print("          |                                     |")
print("          | Bem-vindo ao INSPER - Batalha Naval |")
print("          |                                     |")
print("          =======   xxxxxxxxxxxxxxxxx   ======= ")

time.sleep(0.5)

print("Iniciando o jogo!") 

time.sleep(0.5)

paism, embarcacoesm = random.choice(list(PAISES.items())) #pais sorteado e lista das embarcações disponíveis para tal país

blocos_lista = lista_blocos(embarcacoesm,CONFIGURACAO) #funcao que devolve a lista de blocos disponível por barco disponível

mapa = cria_mapa(10) #precisa mudar a funcao que a variável mapa recebe

mapa_comp = aloca_navios(mapa, blocos_lista) #mapa da máquina 

mapa_jogador= cria_mapa(10)  #Pode ser mudado para mapa(10)

print("O computador está alocando os navios de guerra do país {0}...". format(paism)) 
print("\n")
print("Computador já está em posição de batalha!") 
print("\n")

i=0
for pais in PAISES:
    i += 1
    print("\n")
    print(i, pais)
    for embarcacoes, numero in PAISES[pais].items():
        print("    ", embarcacoes, numero) 

numero_frota = int(input("Qual o número da nação da sua frota?  "))

lista_paises = list(PAISES.keys())

paisjogador = lista_paises[numero_frota-1]

embarcarcoesjogador = PAISES[paisjogador]

blocos_lista_jogador = lista_blocos(embarcarcoesjogador,CONFIGURACAO)

print (embarcarcoesjogador, blocos_lista)
# precisamos fazer uma funcao para aparecer o nome bonitinho junto com os numeros de blocos por navio

alocacao_jogador = aloca_navios_jogador(mapa_jogador, blocos_lista_jogador)

print(mostrar_mapa_comp(mapa_comp,ALFABETO))

print(mostrar_mapa_jog(mapa_jogador,ALFABETO))