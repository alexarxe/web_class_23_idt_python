"""
    Hacer un programa que imprima todos los números enteros que hay desde la unidad hasta un número que introduciremos por teclado.
"""
num = int(input("Ingrese el numero final:  "))

suma =  0
par = 0
impar = 0

for num in range(0, num):
    print(num)
    suma = suma + num
    if num % 2 == 0:
        par = par + num
    else:
        impar = impar + num
print(f"La suma de todos los numero es: {suma}")
print(f"La suma de todos los numeros pares es: {par}")
print(f"La suma de todos los numeros impares es: {impar}")
