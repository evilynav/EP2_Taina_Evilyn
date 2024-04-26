def posicao_suporta(mapa,blocos,linha,coluna,orientacao): 

    #mapa[linha][coluna] 

    if linha < len(mapa): 
        if coluna < len(mapa): 
            if orientacao == 'v': 
                i= 0 #p comecar na linha certa 
                while i< blocos: 
                    if mapa[linha][coluna] == '': 
                        i+=1 #contar o próximo bloco 
                        linha+=1 #passar p linha debaixo

                    else: 
                        return False  

                return True
                    

            elif orientacao == 'h': 
                j=0
                while j < blocos: 
                    if mapa[linha][coluna] == '': 
                        j+=1 
                        coluna+=1 

                    else: 
                        return False 
                return True 