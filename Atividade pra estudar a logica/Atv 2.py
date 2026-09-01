lista=[] 

try:
    for i in range(5):
        print("====Menu====") 
        print("Açai\n uva\n sorvete\n")
    
    produto=input("Qual produtos voce quer?: ")
    lista.extend(produto)
    print(lista) 
    # lista.append(produto)  
except ValueError:
    print("nao temos isso so o que ta no menu")
    
print(f"Seu produtos foram: {lista} obrigado")  
    
    
    
    