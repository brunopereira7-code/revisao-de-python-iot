numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

positivos = []
negativos = []
soma_positivos = 0

for numero in numeros:
    if numero > 0:
        positivos.append(numero)
        soma_positivos += numero
    elif numero < 0:
        negativos.append(numero)

print("Quantidade de positivos:", len(positivos))
print("Quantidade de negativos:", len(negativos))
print("Números negativos:", negativos)
print("Soma dos positivos:", soma_positivos)