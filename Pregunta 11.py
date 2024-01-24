lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_temporal = []
for i in lista_original:
    if i not in lista_temporal:
        lista_temporal.append(i)
lista_original = lista_temporal
print(lista_original)