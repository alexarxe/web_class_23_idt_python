"""
    - Ingresar 5 numeros por teclado y al final de los mismos, el programa debe emitir los siguientes datos: Suma total, 
    Cantidad de numeros impares, y un mensaje que indique si existen números superiores a 100
"""

numOne = input('Ingrese un valor: ')
numTwo = input('Ingrese un valor: ')
numThree = input('Ingrese un valor: ')
numFour = input('Ingrese un valor: ')
numFive = input('Ingrese un valor: ')

def sumar(sumaTotal):
    a = int(numOne)
    b = int(numTwo)
    c = int(numThree)
    d = int(numFour)
    e = int(numFive)

    print('\n_________________Valores ingresados_________________')
    print(f'Primer valor: {a}')
    print(f'Segundo valor: {b}')
    print(f'Tercer valor: {c}')
    print(f'Tercer valor: {d}')
    print(f'Tercer valor: {e}')
    print('------------------------------------------------------')
    sumaTotal = (a + b + c + d + e)
    print(f'Suma total: {sumaTotal} \n**Aqui una suma de los valores ingresados por teclado**')

sumar('sumaTotal')

def impares(a, b, c, d, e):
    a = int(numOne)
    b = int(numTwo)
    c = int(numThree)
    d = int(numFour)
    e = int(numFive)
    
    print('\n_________________Valores impares_________________')

    if a % 2 != 0:
        print(f'Valor Impar:{a}')
    if b % 2 !=0:
        print(f'Valor Impar: {b}')
    if c % 2 !=0:
        print(f'Valor Impar: {c}')

impares('a', 'b', 'c', 'd', 'e')

def identificar(a, b, c, d, e):
    a = int(numOne)
    b = int(numTwo)
    c = int(numThree)
    d = int(numFour)
    e = int(numFive)

    print('\n________________Valores que superan cien____________')

    if a >= 100:
        print(f'El primer valor ingresado es superior a 100. {a}')
    if b >= 100:
        print(f'El segundo valor ingresado es superior a 100. {b}')
    if c >= 100:
        print(f'El tercer valor ingresado es superior a 100. {c}')
    if d >= 100:
        print(f'El cuarto valor ingresado es superior a 100. {d}')
    if e >= 100:
        print(f'El quinto valor ingresado es superior a 100. {e}')

identificar('a', 'b', 'c', 'd', 'e')

print('\n**Programa finalizado**')