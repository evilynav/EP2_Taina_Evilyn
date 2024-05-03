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

print (embarcarcoesjogador, blocos_lista_jogador)

alocacao_jogador = aloca_navios_jogador(mapa_jogador, blocos_lista_jogador)

mapa_jogador = alocacao_jogador

print(mostrar_mapa_comp(mapa_comp,ALFABETO))

print(mostrar_mapa_jog(mapa_jogador,ALFABETO))

#while not foi_derrotado(mapa_jogador) and not foi_derrotado(mapa_comp):

continuar = True
while continuar:
    seleciona_jogador = random.choice(['computador', 'jogador'])
    if seleciona_jogador == 'computador':
        linha_comp = random.randint(0, len(mapa_jogador)-1)
        coluna_comp = random.randint(0, len(mapa_jogador)-1)
        while mapa_jogador[linha_comp][coluna_comp] == X or mapa_jogador[linha_comp][coluna_comp] == A:
            linha_comp = random.randint(0, len(mapa_jogador)-1)
            coluna_comp = random.randint(0, len(mapa_jogador)-1)
        if mapa_jogador[linha_comp][coluna_comp] == N:
            mapa_jogador[linha_comp][coluna_comp] == X
            if foi_derrotado(mapa_jogador) == True:
                print('Que pena, mais sorte na próxima!')
                jogarnovamente = input('você deseja jogar novamente?[s/n]')
                if jogarnovamente == 's':
                    continuar = True
                else:
                    continuar = False
            else:
                mostrar_mapa_comp(mapa_comp,ALFABETO)
                mostrar_mapa_jog(mapa_jogador,ALFABETO)
                seleciona_jogador = 'jogador'
        
        else:
            mapa_jogador[linha_comp][coluna_comp] == A
            mostrar_mapa_comp(mapa_comp,ALFABETO)
            mostrar_mapa_jog(mapa_jogador,ALFABETO)
            seleciona_jogador = 'jogador'
    else:
        linha_jog = int(input('digite a linha de ataque: '))-1
        coluna_jog = int(input('digite a coluna de ataque: '))
        while mapa_comp[linha_jog][coluna_jog] == X or mapa_comp == A:
            linha_jog = int(input('digite a linha de ataque: '))-1
            coluna_jog = int(input('digite a coluna de ataque: '))
        if mapa_comp[linha_jog][coluna_jog] == N:
            mapa_comp[linha_jog][coluna_jog] = X
            if foi_derrotado(mapa_comp) == True:
                print('Parabéns, você venceu a batalha! =)')
                jogarnovamente = input('você deseja jogar novamente?[s/n]')
                if jogarnovamente == 's':
                    continuar = True
                else:
                    continuar = False

            else:
                mostrar_mapa_comp(mapa_comp,ALFABETO)
                mostrar_mapa_jog(mapa_jogador,ALFABETO)
                seleciona_jogador = 'computador'
        else:
            mapa_comp[linha_jog][coluna_jog] = A
            mostrar_mapa_comp(mapa_comp,ALFABETO)
            mostrar_mapa_jog(mapa_jogador,ALFABETO)
            seleciona_jogador = 'computador'

