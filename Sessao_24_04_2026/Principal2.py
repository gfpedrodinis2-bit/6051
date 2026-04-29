# produtos da maquina



config = {
    "produtos" : {
        "café curto" :{
            "preço" : "0.5",
            "tem_palheta" :True,
            "tem_acucar" : True,
            "nivel_de_acucar" : 2,
            "tem_copo" :True
        },
        "café longo" : {
            "preço" : "0.5",
            "tem_palheta" :True,
            "tem_acucar" : True,
            "nivel_de_acucar" : 2,
            "tem_copo" :True,
            "botao_cafe_longo" : "periferico 2"
        },
        "cha" :{
            "preço" : "0.2",
        },
        "cappucino" : {
            "preço" : "0.5",
        },
        }
    
    }

config ["produtos"]
config ["produtos"]["cha"]
preco_do_cha = config ["produtos"]["cha"]["preço"]
config["produtos"]["café longo"]["nivel_de_acucar"]

config_da_maquina = {
    "velocidade"
}

botao_cafe_longo = config["produtos"]["café longo"]["botao_cafe_longo"]


#ciclo principal

while True:

    # dados de entrada

    velocidade_da_maquina = config_da_maquina ["velocidade"]



    # processamento

    if botao_cafe_longo and dinheiro_certo:
        if config["produtos"]["café longo"]["tem_copo"]:
            colocar_copo()
        else:
            nao_colocar_copo()


    if botao_tirar_acucar :
        if config["produtos"]["cafe longo"]["nivel_de_acucar"] > 0:
            config ["produtos"]["cafe longo"]["nivel_de_acucar"] -= 1

def colocar_copo():
    """codigo para pedir à maquina para tirar copo"""
    print("Tirar copo")