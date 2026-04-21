# ciclo principal

while True:

# dados de entrada
    sensor_humidade = 5
    planta = 2                            # Cacto <-2
    tempo = 75                            # Horas

# Processamento
    if sensor_humidade < 10 and planta == 2 and tempo > 72 :
        liga_rega = True
    else:
        liga_rega = False