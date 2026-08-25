import os 
os.system("cls")

temperatura=[] 

for x in range(5):
    temp=float(input(f"digite {x+1} temperatura: ")) 
    temperatura.append(temp) 
    
    media=sum(temperatura)/len(temperatura)
    menor=min(temperatura) 
    maior=max(temperatura) 
    
print(f"a maior temperatura do dia foi {maior}ºC") 
print(f"a menor temperatura do dia foi {menor}ºC") 
print(f"a media temperatura do dia foi {media:.1f}ºC") 
    
    