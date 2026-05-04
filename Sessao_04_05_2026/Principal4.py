import tkinter as tk
from PIL import Image, ImageTk  # Necessário instalar: pip install Pillow

def criar_pagina():
    root = tk.Tk()
    root.title("Minha Página em Python")
    root.geometry("600x800")

    # 1. NOME EM LETRAS GRANDES (Topo)
    titulo = tk.Label(
        root, 
        text="Pedro Ferreira", 
        font=("Arial", 40, "bold"), 
        pady=20
    )
    titulo.pack()

    # 2. FOTO (Meio da página)
    # Certifica-te que tens uma imagem chamada 'foto.jpg' na mesma pasta do código
    try:
        img_aberta = Image.open("foto.jpg")
        img_redimensionada = img_aberta.resize((199, 204)) # Ajusta o tamanho
        foto = ImageTk.PhotoImage(img_redimensionada)
        
        label_foto = tk.Label(root, image=foto)
        label_foto.image = foto # Mantém uma referência da imagem
        label_foto.pack(pady=20)
    except:
        label_erro = tk.Label(root, text="[Imagem não encontrada - coloca 'foto.jpg' na pasta]")
        label_erro.pack(pady=20)

    # 3. LISTA DE COISAS (Fim)
    label_lista_titulo = tk.Label(root, text="UFCD Eletricidade:", font=("Arial", 14, "underline"))
    label_lista_titulo.pack(pady=10)

    itens = [
        "UFCD 6 → Transístores bipolares",
        "UFCD 7 → Eletrónica de potência – dispositivos",
        "UFCD 8 → Circuitos lógicos",
        "UFCD 9 → Circuitos combinatórios",
        "UFCD 10 → Circuitos sequenciais assíncronos",
        "UFCD 11 → Técnicas de montagem de circuitos eletrónicos",
        "UFCD 12 → Sistemas trifásicos",
        "UFCD 13 → Transformadores",
        "UFCD 14 → Máquinas elétricas rotativas e variadores de velocidade",
        "UFCD 15 → Sistemas e técnicas de medida",
        "UFCD 16 → Gestão da manutenção – introdução",
        "UFCD 17 → Noções de manutenção e trabalho em eletricidade e eletrónica",
        "UFCD 20 → Instalações elétricas – generalidades",
        "UFCD 29 → Automatismos eletromecânicos – contactores (aplicações)",
        "UFCD 46 → Organização laboral"
    ]

    for item in itens:
        label_item = tk.Label(root, text=item, font=("Arial", 12))
        label_item.pack(anchor="w", padx=20) # Alinha à esquerda com margem

    root.mainloop()

if __name__ == "__main__":
    criar_pagina()