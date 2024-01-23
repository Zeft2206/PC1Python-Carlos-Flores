time = input("Ingresa la hora: ")
hours,minute = time.split(":")
if int(hours) >= 7 and int(hours) < 8 and int(minute) >= 00 and int(minute) <= 59:
    print("Hora del desayuno")
elif int(hours) >= 12 and int(hours) < 13 and int(minute) >= 00 and int(minute) <= 59:
    print("Hora del almuerzo")
elif int(hours) >= 18 and int(hours) < 19 and int(minute) >= 00 and int(minute) <= 59:
    print("Hora de la cena")
else:
    print(" ")

