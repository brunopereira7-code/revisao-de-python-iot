import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def resultado():
    
    try:
        nome=nome.get()
        nota1=float(n1.get())
        nota2=float(n2.get())
        
        media=(nota1+nota2)/3
        
        
        
        if media<5:
            situacao="Reprovado"
        else:
            situacao="Aprovado"

        resultado2.configure(text=f'resultado final:{situacao}',text_color="red" if media <5 else 'green')
        
        resultado1.configure(text=f'Media final:{media:.1f}')    
    except:
        resultado1.configure(text="Digite valores validos")
        resultado2.configure(text="Resultado final",text_color="white")
         
        
        

import os 
os.system("cls") 

janela=ctk.CTk()
janela.geometry("600x500")
janela.resizable(False,False)
janela.title("Resultado Academico")


titulo=ctk.CTkLabel(
    janela,
    text="Resultado Academico",
    text_color="white",
    font=("Arial",20)
)

titulo.pack()


nome=ctk.CTkEntry(
    janela,
    placeholder_text="Digite o nome do aluno",
    width=400,
    
)
nome.pack(pady=15)

n1=ctk.CTkEntry(
    
    janela,
    placeholder_text="Digite a nota 1",
    width=400,
    height=30,
    
    
)
n1.pack(pady=15)

n2=ctk.CTkEntry(
    
    janela,
    placeholder_text="Digite a nota 2",
    width=400,
    height=30,
)

n2.pack(pady=15)


botao=ctk.CTkButton(
    janela,
    text="Calcular",
    width=200,
    height=30,
    text_color="white",
    cursor="hand2",
    font=("Arial",15),
    command=resultado
)

botao.pack(pady=20)

resultado1=ctk.CTkLabel(
    janela,
    text="media",
    text_color="white",
    font=("Arial",15)
)

resultado1.pack(pady=10)

resultado2=ctk.CTkLabel(
    janela,
    text="Resultado",
    text_color="white",
    font=("Arial",15)
)
resultado2.pack(pady=10)


janela.mainloop()
