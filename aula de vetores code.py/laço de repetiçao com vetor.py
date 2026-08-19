carrinho =[] 

while True: 
    produto = float(input("digite o valor do produto:")) 
    if(produto == 0):
        break 
    else:
        carrinho.append(produto) 
        
    total=sum(carrinho) 
    print(f"o valor total é R${total:.2f}") 
    