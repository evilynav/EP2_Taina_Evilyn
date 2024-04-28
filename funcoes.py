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
    

    #Tentativa de realizar commit