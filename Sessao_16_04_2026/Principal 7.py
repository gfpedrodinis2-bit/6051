# ciclo principal

while True:
    
    #dados de entrada
    Interruptor_1 = 0
    Interruptor_2 = 0
    Interruptor_3 = 1
    Interruptor_4 = 0

    # processamento
    if  Interruptor_1 ==1 or Interruptor_2 ==1 or Interruptor_3  ==1 or Interruptor_4 == 1:
        liga_led = True
    else:
        liga_led = False