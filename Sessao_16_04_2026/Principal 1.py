# ciclo principal

while True:
    # dados de entrada
    sensor_pressão = 35

    # Processamento
    if sensor_pressão >= 40:
        ativa_eletrovalvula = True
    else:
        ativa_eletrovalvula = False