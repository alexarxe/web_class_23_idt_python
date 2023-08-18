"""
    Hacer un programa que imprima y cuente los múltiplos de 3 que hay entre los numeros que introduciremos por teclado 
"""
i = int(input("Ingrese el numero inicial:  "))
f = int(input("Ingrese el numero final:  "))
suma = 0
print("Los numeros pares del rango")
while i <= f:
    if i % 3 == 0:
        print(i)
        suma = suma + i
    i+=1
print(f"\nLa suma de los numeros:  {suma}")