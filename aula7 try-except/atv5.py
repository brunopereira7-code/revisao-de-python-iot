import os 
os.system("cls") 

try:
    saldo=float(input("digite o saldo da sua conta: ")) 
    saque=float(input("digite o valor do saque: ")) 
    
    if saque<=0:
        print("Saque invalido") 
        
    elif saque>saldo:
        print("Saldo insuficiente") 
    else:
        saldo=saldo-saque 
        print(f"saque realizado com sucesso, seu saldo atual é {saldo:.2f}")    
        print(f"Saldo restante: {saldo:.2f}")
except:
    print("erro digite apenas numeros")
