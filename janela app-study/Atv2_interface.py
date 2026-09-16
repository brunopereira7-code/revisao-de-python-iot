
import customtkinter as ctk

ctk.set_appearance_mode('dark')
#funções-------------------------------------------------------
def calcular():
    d=int(distancia.get())
    c=float(consumo.get())
    p=float(preco.get())
    
    formula=(d/c)*p
    resultado.configure(text=f'o gasto da vigaem sera de R$ {formula:.2f}')

#janela
janela = ctk.CTk()
janela.geometry("500x400")
janela.resizable(False,False)
janela.title('Calculadora de Viagem')
janela.iconbitmap('car_23964.ico')
#------------------------------------

titulo = ctk.CTkLabel(janela,
                      text='APP DE VIAGEM',
                      text_color='white',
                      font=('Verdana',45,'bold'),)
titulo.pack()

distancia = ctk.CTkEntry(janela,
                         width=400,
                         height=40,
                         border_color='white',
                         placeholder_text='Digite a distância da viagem em KM',)
distancia.pack(pady = 20)


consumo = ctk.CTkEntry(janela,
                       width=400,
                       height=40,
                       border_color='white',
                       placeholder_text='Digite o consumo do seu veículo',)
consumo.pack(pady=20)


preco = ctk.CTkEntry(janela,
                       width=400,
                       height=40,
                       border_color='white',
                       placeholder_text='Digite o consumo do seu veículo',)
preco.pack(pady=20)


botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text='Calcular Gasto',
                      fg_color='#fa7f84',
                      border_width=2,
                      border_color="#ff0008",
                      text_color='black',
                      cursor = 'hand2',
                      font=('times new Roman',15,'bold'),
                      command=calcular,
                      )
botao.pack(pady=30)

resultado=ctk.CTkLabel(janela,
                       text='', 
                       text_color='white',
                       font=('Arial',20),)
resultado.pack(pady=10)




janela.mainloop()
