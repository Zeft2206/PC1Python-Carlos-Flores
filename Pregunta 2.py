
costo = float(input("Ingrese el costo de la comida: "))
porcentaje_de_propina = float(input("Ingrese cuanta propina desea dejar: "))
if porcentaje_de_propina >= 0.15:
    propina = costo * porcentaje_de_propina
else:
    print("Ingrese otro porcentaje de propina")
print(f'La propina a dejar es {propina} ')

