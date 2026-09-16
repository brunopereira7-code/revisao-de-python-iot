import os
import customtkinter as ctk 
ctk.set_appearance_mode('dark')

janela=ctk.CTk() 
janela.geometry("500x300") 
janela.resizable(False,False) 
janela.title("App De Viagem") 
janela.iconbitmap("car_23964.ico") 


titulo=ctk.CTkLabel(janela,
                    text="App De Viagem",
                    text_color="white",
                    font=("Arial", 30, "bold"))
titulo.pack() 


login=ctk.CTkEntry(janela,
                   width=400,
                   height=30,
                   border_color=("#f5e9e9"),
                   placeholder_text="Digite Seu Login") 
 
login.pack(pady=30) 

senha=ctk.CTkEntry(janela,
                   width=400,
                   height=30,
                   border_color=("#f5e9e9"),
                   placeholder_text="Digite Sua Senha",
                   show="*") 
senha.pack(pady=10) 

preco=ctk.CTkEntry(janela,
                    width=400,
                    height=30,
                    border_color=("#f5e9e9"),
                    placeholder_text="Digite o Preço da Viagem",
                    text_color="white",
                    font=("Arial", 14)) 
preco.pack(pady=15)


botao=ctk.CTkButton(janela,
                    text="Entrar",
                    width=200,
                    height=30,
                    border_color=("#d41313"),
                    cursor="hand2",
                    command=lambda: print("Entrando...")) 

botao.pack(pady=20) 

janela.mainloop()