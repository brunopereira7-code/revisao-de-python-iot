import customtkinter as ctk 
import os 
 

ctk.set_appearance_mode('dark') 



def calcular_hospedagem():
    try:
        
        qtd_diarias = int(diarias.get())
        preco_diaria = float(valor_diaria.get().replace(',', '.'))
        
        valor_hospedagem = qtd_diarias * preco_diaria
        
        if qtd_diarias >= 5:
            valor_desconto = valor_hospedagem * 0.10
        else:
            valor_desconto = 0.0
            
        total_pagar = valor_hospedagem - valor_desconto
        
        
        str_hospedagem = f'R$ {valor_hospedagem:.2f}'.replace('.', ',')
        str_desconto = f'R$ {valor_desconto:.2f}'.replace('.', ',')
        str_total = f'R$ {total_pagar:.2f}'.replace('.', ',')
        
        resultado_hospedagem.configure(text=f'Hospedagem: {str_hospedagem}')
        resultado_desconto.configure(text=f'Desconto: {str_desconto}')
        resultado_total.configure(
            text=f'Total a Pagar: {str_total}',
            text_color='#32CD32' 
        )
        
    except ValueError:
        resultado_hospedagem.configure(text='Erro nos dados inseridos')
        resultado_desconto.configure(text='-')
        resultado_total.configure(
            text='Total a Pagar: -',
            text_color='white'
        )        

janela = ctk.CTk()
janela.geometry("600x650") 
janela.resizable(False,False) 
janela.title("Sistema de Reserva de Hotel")

titulo = ctk.CTkLabel(
    janela,
    text="Reserva de Hotel",
    
    font=('arial', 35, 'bold')
) 
titulo.pack(pady=(20, 10)) 


hospede = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    
    placeholder_text='Digite o nome do hóspede'
)
hospede.pack(pady=15)


diarias = ctk.CTkEntry(
    janela,
    width=400,
    height=40,

    placeholder_text='Digite a quantidade de diárias'
)
diarias.pack(pady=15)

valor_diaria = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    placeholder_text='Digite o valor da diária'
)
valor_diaria.pack(pady=15)


botao = ctk.CTkButton(
    janela,
    width=400,
    height=40,
    text='CALCULAR HOSPEDAGEM',
    text_color='black',
    cursor='hand2',
    font=('arial', 20, 'bold'),
    command=calcular_hospedagem
) 
botao.pack(pady=25)

resultado_hospedagem = ctk.CTkLabel(
    janela,
    text='Hospedagem: -',
    text_color='white',
    font=("Arial", 20)
) 
resultado_hospedagem.pack(pady=5)

resultado_desconto = ctk.CTkLabel(
    janela,
    text='Desconto: -',
    text_color='white',
    font=("Arial", 20)
) 
resultado_desconto.pack(pady=5)

resultado_total = ctk.CTkLabel(
    janela,
    text='Total a Pagar:',
    text_color='white',
    font=("Arial", 25, "bold")
) 
resultado_total.pack(pady=10)

janela.mainloop()