from math import trunc

print('prueba del for')
for i in range(5):
    print(i)

print('PRUEBA DEL WHILE')
contador = 0
while contador < 5:
    print(contador)
    contador += 1

contador = 1.5
print(contador)
contador = True
print(contador)
contador = 'cualquier'
print(contador)

print('pruebas arr')
lista1 = [1,2,3,'hola',True]
for indice in lista1:
    print(indice)
lista1[4] = 'mundo'
lista1[2] = 'buenas,'
for i in lista1:
    print(i)

def saludar(nombre):
    print("Hola,", nombre)

saludar("Joaquin")  # Llamada a la función