def mostrar_mapa(mapa_cpu,mapa_player,n): 
    print("COMPUTADOR- {0}") 
    
    linha= " " 
    for i in range (n): 
        linha+= " "+ALFABETO+" " 
        esp= " "*2+linha+" "*2 
        print(esp) 