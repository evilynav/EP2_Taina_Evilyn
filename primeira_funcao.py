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