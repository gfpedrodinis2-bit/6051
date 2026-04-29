import tkinter

raiz= tkinter.Tk()

texto = tkinter.Entry()
texto.pack()

def Ligar_lampada_1():
    print("Ola")

def Ligar_lampada_2():
    print("Testar")

## criar o botao
botao0 = tkinter.Button(text= "Botao_0", command=Ligar_lampada_1)
botao1 = tkinter.Button(text= "Botao_1", command=Ligar_lampada_2)
botao2 = tkinter.Button(text= "Botao_2")
botao3 = tkinter.Button(text= "Botao_3")
botao4 = tkinter.Button(text= "Botao_4")
botao5 = tkinter.Button(text= "Botao_5")
botao6 = tkinter.Button(text= "Botao_6")
botao7 = tkinter.Button(text= "Botao_7")
botao8 = tkinter.Button(text= "Botao_8")
botao9 = tkinter.Button(text= "Botao_9")



## envia-lo para o interface
botao0.pack()
botao1.pack()
botao2.pack()
botao3.pack()
botao4.pack()
botao5.pack()
botao6.pack()
botao7.pack()
botao8.pack()
botao9.pack()


# arrancar com o interface
raiz.mainloop()