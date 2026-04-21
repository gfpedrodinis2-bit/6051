### media de vendas

vendas_segunda_feira = 20
vendas_terca_feira = 33
vendas_quarta_feira = 22
vendas_quinta_feira = 28
vendas_sexta_feira = 26
vendas_sabado = 12
vendas_domingo = 40
numero_de_dias =7

media_vendas = (vendas_segunda_feira + vendas_terca_feira + vendas_quarta_feira + vendas_quinta_feira + vendas_sexta_feira + vendas_sabado + vendas_domingo) / numero_de_dias
print(media_vendas)

### dias em que as estao acima da media

if  vendas_segunda_feira - media_vendas > 0 :
    valor1 = 1
    print("Dia Bom")
else:
    print("Dia mau")
    valor1 = 0


if vendas_terca_feira - media_vendas > 0 :
    valor2 = 1
    print("Dia Bom")
else:
    print("Dia mau")
    valor2 = 0


if vendas_quarta_feira - media_vendas > 0 :
    valor3 = 1
    print("Dia Bom")
else:
    print("Dia mau")
    valor3 = 0

 
if vendas_quinta_feira - media_vendas > 0 :
    valor4 = 1
    print("Dia Bom")
else:
    print("Dia mau")
    valor4 = 0

if vendas_sexta_feira - media_vendas > 0 :
    valor5 = 1
    print("Dia Bom")
else:
    print("Dia Mau")
    valor5 = 0

if vendas_sabado - media_vendas > 0 :
    valor6 = 1
    print("Dia Bom")
else:
    print("Dia Mau")
    valor6 = 0

if vendas_domingo - media_vendas > 0 :
    valor7 = 1
    print("Dia Bom")
else:
    print("Dia Mau")
    valor7 = 0


    ## total de dias bons


dias_bons = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7
print(dias_bons)