notas = []

for i in range(8):
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

acima_da_media = []

for nota in notas:
    if nota > media:
        acima_da_media.append(nota)

print("Notas:", notas)
print("Média da turma:", media)
print("Notas acima da média:", acima_da_media)