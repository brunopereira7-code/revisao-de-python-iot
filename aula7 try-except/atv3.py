import os 
os.system("cls") 

while True:
    try:
        numeros=int(input("digite um numero: "))
        
        for i in range(1,11): 
            print(numeros,"x",i,"=",numeros*i) 
    
        
        break
    
    
    
    except:
        print("erro  digite apenas numeros")