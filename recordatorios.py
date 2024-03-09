import sys

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Output
# print(recordatorios)
#año-mes-dia
fecha1 = ['2021-02-01', "06:00", "Empezar el día"]
recordatorios.insert(1, fecha1)
print(recordatorios)

recordatorios[3][0] = '2021-07-16'
print(recordatorios)

recordatorios.pop(2)
print(recordatorios)

cena_navidad = ['2021-12-24', "22:00", "Cena de Navidad"]
recordatorios.insert(4, cena_navidad)
print(recordatorios)

cena_añonuevo = ['2021-12-31', "22:00", "Cena Año Nuevo"]
recordatorios.insert(6, cena_añonuevo)
print(recordatorios)

for elemento in recordatorios:
    print(elemento)

