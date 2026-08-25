import os 
os.system("cls")
numeros=[] 
soma=0
while True:
    try:
        num=int(input("Digite o numero")) 
        if (num == 0):
            break 
        
        numeros.append(num) 
        soma+=num
    except ValueError:
        print("Erro digite numeros") 
        
        
# print("numeros digitados",numeros) 
print("Soma",soma)