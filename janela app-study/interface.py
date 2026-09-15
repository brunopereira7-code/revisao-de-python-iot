import customtkinter as ctk 
ctk.set_appearance_mode('dark')


janela=ctk.CTk()  
janela.geometry('500x300')
janela.resizable(False,False) 
#pra nao redirencionar a tela
janela.title('Sistema de acesso - 2026') 
janela.iconbitmap('security-protection-protect-key-password-login_108554.ico') 

#arrasta a imagem pro codigo e segura shift e coloca dentro dos parenteses
#o site do icone é icon icons
# pip install customtkinter
#----------------------------------------------------------------------------------------- 

#corpo da janela----------------------  

titulo=ctk.CTkLabel(janela, 
                    text='Sistema de login',
                    text_color='#0ffa79',
                    font=('arial',40)) 
#pra ver a cor color picker e copiar o codigo da cor
titulo.pack()


login=ctk.CTkEntry(janela,
                   width=400,
                   height=40,
                   border_color='#0ffa79',
                    placeholder_text='Digite seu login')

login.pack(pady=30) 


senha=ctk.CTkEntry(janela,
                   width=400,
                   height=40,
                   border_color='#0ffa79',
                    placeholder_text='Digite sua senha', 
                    show='*')

senha.pack()  

botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text='Acessar',
                      fg_color='#0ffa79',
                      text_color='white',
                      cursor='hand2',
                      font=('arial',30)
                      ) 
botao.pack(pady=30)













janela.mainloop() 



