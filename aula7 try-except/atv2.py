import os 
os.system("cls")

try:
    idade=int(input("digite sua idade: "))
    
    if (idade>=18):
        print("voce é maior de idade")
    else:
        print("voce é menor de idade")    
except:
    print("erro  digite apenas numeros") 
    


    
