#Primeira função: cria_mapa 

def cria_mapa(dimensao): 
    lista_final= [] 
    listinha= [] 

    i=0 
    while i < dimensao: 
        listinha.append(' ')
        i+=1 

    j=0
    while j < dimensao: 
        lista_final.append(listinha)
        j+=1 

    return lista_final 

#segunda função: posicao_suporta

def posicao_suporta(mapa,blocos,linha,coluna,orientacao): 

    #mapa[linha][coluna] 

            if orientacao == 'v': 
                    for i in range(blocos): 
                        if (linha+i) >= len(mapa): 
                            return False
                        elif mapa[linha+i][coluna] == 'N': 
                            return False 
                            
            elif  orientacao == 'h': 
                for j in range(blocos): 
                    if (coluna+j) >= len(mapa):
                        return False 
                    
                    elif mapa[linha][coluna+j] == 'N': 
                         return False 
            return True 

#Terceira função: 

def aloca_navios (mapa, blocos):
    n = len(mapa)
    #escolha das variáveis pela máquina:
    
    for size_navio in blocos:
        linha = random.randint(0, n-1)
        coluna = random.randint(0, n-1)
        orientacao = random.choice(['h', 'v'])

        while not posicao_suporta(mapa, size_navio, linha, coluna, orientacao):
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])

        if orientacao == 'h':
            for j in range(coluna, size_navio + coluna):
                mapa[linha][j] = 'N'
        else:
            for i in range(linha, size_navio+ linha):
                mapa[i][coluna] = 'N'
    return mapa



#Quarta função: foi_derrotado

#a matriz pode ser de qualquer dimensão;
#cada elemento de raiz quadrada é um caracter;
#a função retorna False caso houver um 'N' como caracter, pois significa que ainda existem navios na matriz;

def foi_derrotado (matriz_quadrada):
    i = 0
    navio = 0
    while i < len(matriz_quadrada):
        j = 0
        while j < len(matriz_quadrada[i]):
            if matriz_quadrada[i][j] == 'N':
                navio +=1
            else:
                navio = navio
            j += 1
        i +=1
    if navio == 0:
        return True
    else:
        return False 
    
import random
def aloca_navios (mapa, blocos):
    n = len(mapa)
    #escolha das variáveis pela máquina:
    
    for size_navio in blocos:
        linha = random.randint(0, n-1)
        coluna = random.randint(0, n-1)
        orientacao = random.choice(['h', 'v'])

        while not posicao_suporta(mapa, size_navio, linha, coluna, orientacao):
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])

        if orientacao == 'h':
            for j in range(coluna, size_navio + coluna):
                mapa[linha][j] = 'N'
        else:
            for i in range(linha, size_navio+ linha):
                mapa[i][coluna] = 'N'
    return mapa


#função escolher frota: escolher_frota 
def escolher_frota(numero_frota): 
    if numero_frota == 1: 
        mensagem = "Você escolheu a nação Brasil!"
        espaco = "\n"  
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print(mensagem, espaco, mensagem_alocar) 
    
    elif numero_frota == 2: 
        mensagem = "Você escolheu a nação França!" 
        espaco = "\n"
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem,espaco, mensagem_alocar)  
    
    elif numero_frota == 3: 
        mensagem = "Você escolheu a nação Austrália!" 
        espaco = "\n"
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem,espaco, mensagem_alocar)
    
    elif numero_frota == 4: 
        mensagem = "Você escolheu a nação Rússia!" 
        espaco = "\n"
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem, espaco, mensagem_alocar)
    
    elif numero_frota == 5: 
        mensagem = "Você escolheu a nação Japão!" 
        espaco = "\n"
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem, espaco, mensagem_alocar) 
    

#Função lista_blocos 

def lista_blocos  (embarcacoes,dic_conf):
    quant_emb = list(embarcacoes.values()) #quantas embarcações temos de cada tipo disponível para o país
    nome_embarcacao = list(embarcacoes.keys()) # nomes das embarcações usados para encontrar quantos blocos cada uma ocupa
    lista_b = list(dic_conf.items()) #lista (nome_barco,numero_blocos) do dicionario
    lista_pp = [] #lista que ordena a quantidade de blocos por barco disponível
    lista_nome = [] #lista com nomes repetidos

    indice = 0
    while indice < len(nome_embarcacao):
        indice2 = 0
        while indice2 < quant_emb[indice]:
            lista_nome.append(nome_embarcacao[indice])
            indice2 += 1
        indice += 1


    i = 0
    while i < len(lista_nome):
        barco = lista_nome[i]
        j = 0
        while j < len(lista_b):
            if barco == lista_b[j][0]:
                lista_pp.append(lista_b[j][1])
            j += 1
        i += 1 

        
    return lista_pp

