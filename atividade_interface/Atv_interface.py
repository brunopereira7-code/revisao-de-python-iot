import customtkinter as ctk 
#python -m pip install customtkinter pra baixar caso der falha

ctk.set_appearance_mode('dark') 

#função 
def resultado():
    try:
        nota1 = float(n1.get())
        nota2 = float(n2.get())
        nota3 = float(n3.get())
        
        media = (nota1 + nota2 + nota3) / 3
        
        # Primeiro verificamos a situação do aluno
        if media < 5: 
            situacao = 'Recuperação' 
        else: 
            situacao = 'Aprovado' 
        
        resultado2.configure(
            text=f'resultado final: {situacao}',
            text_color='red' if media < 5 else 'green'
        )
        
        resultado1.configure(
            text=f'media: {media:.1f}'
        )
        
    except:
        resultado1.configure(
            text='dado invalido'
        )
        
        resultado2.configure(
            text='resultado final: -',
            text_color='white'
        )
        
            
import os 
os.system("cls") 

janela = ctk.CTk()
janela.geometry("600x500") 
janela.resizable(False,False) 
janela.title("Sistema Escolar")

titulo = ctk.CTkLabel(
    janela,
    text="Sistema Escolar",
    text_color='yellow',
    font=('arial',40)
) 
titulo.pack() 

# Nota 1
n1 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color='yellow',
    placeholder_text='Digite a primeira nota'
)
n1.pack(pady=15)

# Nota 2
n2 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color='yellow',
    placeholder_text='Digite a segunda nota'
)
n2.pack(pady=15)

# Nota 3
n3 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    border_color='yellow',
    placeholder_text='Digite a terceira nota'
)
n3.pack(pady=15)

botao = ctk.CTkButton(
    janela,
    width=400,
    height=40,
    text='Calcular Média',
    fg_color='yellow',
    text_color='black',
    cursor='hand2',
    font=('arial',30),
    hover_color="#BEDA23",
    #se voce digitar #ffff aparece a cor pra mudar dentro do vs conde
    command=resultado
) 

botao.pack(pady=20)

resultado1 = ctk.CTkLabel(
    janela,
    text='media:',
    text_color='white',
    font=("Arial",25)
) 

resultado1.pack(pady=10)

resultado2 = ctk.CTkLabel(
    janela,
    text='resultado final:',
    text_color='white',
    font=("Arial",25)
) 

resultado2.pack(pady=10)


janela.mainloop()