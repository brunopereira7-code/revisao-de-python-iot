import os 
os.system("cls") 

lista=[]
while True:
    print("Caso acabe digite fim\n")
    nome=input("digite os nomes: ")
    
    if nome =="fim":
        break 
    lista.append(nome)
lista.sort() 
print("os nomes sao ",lista)
print("quantidade de nomes", len(lista))
