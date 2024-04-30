import time 
from base_geral import * 
from funcao_escfrota import * 
import random
from primeira_funcao import cria_mapa
from terceira_funcao import posicao_suporta
from terceira_funcao import aloca_navios
from define_blocos import lista_blocos

print("=================================") 
print("Bem-vindo ao INSPER-Batalha Naval!!") 
print("=================================") 

time.sleep(0.5)

print("Iniciando o jogo!") 

time.sleep(0.5)

paism, embarcacoesm = random.choice(list(PAISES.items())) #pais sorteado e lista das embarcações disponíveis para tal país

blocos_lista = lista_blocos(embarcacoesm,CONFIGURACAO) #funcao que devolve a lista de blocos disponível por barco disponível

mapa = cria_mapa(10) #precisa mudar a funcao que a variável mapa recebe

mapa_comp = aloca_navios(mapa, blocos_lista) #mapa da máquina

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
print(escolher_frota(numero_frota))

#printar os mapas vazios




