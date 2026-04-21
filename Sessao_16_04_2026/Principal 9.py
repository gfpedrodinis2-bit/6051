# Exercício : 2 Janelas

# loop principal
while True:
    #dados de entrada
    #Janela com valores em percentagem
    Janela1 = 50 # valor pode ir de 0% a 100%
    Janela2 = 40 # valor pode ir de 0% a 100%

    # janela > 10 significa que quero verificar
    # se a janela não esta totalmente fechada
    if Janela1 > 10 and Janela1 < 90 :
        print(" janela 1 ok")
    else:
        print(" janela 1 Erro ")


    # Janela 2
    if Janela2 > 10 and Janela2 < 90 :
        print("janela 2 OK")
    else:
        print  ("janela 2 Erro")