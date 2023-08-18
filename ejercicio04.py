"""
    Hacer un programa que imprima los números impares entre el 10 y el cero en orden decreciente y que calcule la suma de esos números impares.
"""
i = int(input("Ingrese el numero inicial:  "))
f = int(input("Ingrese el numero final:  "))
suma = 0
print("Los numeros impares del rango")
while i <= f:
    if i % 2 != 0:
        print(i)
        suma = suma + i
    i+=1
print(f"\nLa suma de los numeros:  {suma}")