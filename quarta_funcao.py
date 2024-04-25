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
