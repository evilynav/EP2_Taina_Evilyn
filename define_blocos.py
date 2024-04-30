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
