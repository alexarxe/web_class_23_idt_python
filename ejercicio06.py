#Introducir por teclado tantas frases como se deseen y contarlas

while True:
    frase = input("Ingrese un texto:\n")
    text = frase
    substring = frase

    total_occurrences = text.count(substring)

    print("There are " + str(total_occurrences) + " occurrences.")
