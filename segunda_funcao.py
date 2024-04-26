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