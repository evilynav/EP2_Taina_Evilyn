import time 
from base_geral import * 
from funcao_escfrota import * 
import random
from primeira_funcao import cria_mapa
from terceira_funcao import posicao_suporta
from terceira_funcao import aloca_navios

print("=================================") 
print("Bem-vindo ao INSPER-Batalha Naval!!") 
print("=================================") 

time.sleep(0.5)

print("Iniciando o jogo!") 

time.sleep(0.5)

paism, embarcacoes = random.choice(list(PAISES.items())) #pais sorteado e lista das embarcações disponíveis para tal país

mapa = cria_mapa(10)

quant_emb = embarcacoes.values() #quantas embarcações temos de cada tipo disponível para o país

nome_embarcacao = embarcacoes.keys() # nomes das embarcações usados para encontrar quantos blocos cada uma ocupa


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

print("Agora é a sua vez de alocar seus navios de guerra.") 

numero_frota = int(input("Qual o número da nação da sua frota?  ")) 
print(escolher_frota(numero_frota))





