import os 
os.system("cls") 


try:
    nota1=float(input("digite a primeira nota: "))
    nota2=float(input("digite a segunda nota: "))
    nota3=float(input("digite a terceira nota: "))
    media=(nota1+nota2+nota3)/3 
    
    if (media>=7):
        print(f"voce foi aprovado com a media {media:.2f}")
        
    elif (media >=5):
        print(f"voce esta de recuperação com a media {media:.2f}")
    else:
        print(f"voce foi reprovado com a media {media:.2f}")
    
except:
    print("erro digite apenas numeros")
