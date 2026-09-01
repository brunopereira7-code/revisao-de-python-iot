
import os 
os.system("cls")

lista=[]

for i in range(6):
        numeros=int(input("Digite os seis numeros"))
        lista.append(numeros) 
        
print("soma", sum(numeros)) 
print("Maior valor", max(numeros)) 
print("Menor valor", min(numeros)) 

numeros.sort() 
print("numeros em ordem crescente",numeros)
    
    