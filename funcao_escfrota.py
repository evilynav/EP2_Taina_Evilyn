numero_frota = int(input("Qual o número da nação da sua frota?  ")) 

def escolher_frota(numero_frota): 
    if numero_frota == 1: 
        mensagem = "Você escolheu a nação Brasil!"
        espaco = "\n"  
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print(mensagem, espaco, mensagem_alocar) 
    
    elif numero_frota == 2: 
        mensagem = "Você escolheu a nação França!" 
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem,espaco, mensagem_alocar)  
    
    elif numero_frota == 3: 
        mensagem = "Você escolheu a nação Austrália!" 
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem,espaco, mensagem_alocar)
    
    elif numero_frota == 4: 
        mensagem = "Você escolheu a nação Rússia!" 
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem, espaco, mensagem_alocar)
    
    elif numero_frota == 5: 
        mensagem = "Você escolheu a nação Japão!" 
        mensagem_alocar = "Agora é a sua vez de alocar os seus navios!" 
        print (mensagem, espaco, mensagem_alocar) 
    
print(escolher_frota(numero_frota)) 

        

