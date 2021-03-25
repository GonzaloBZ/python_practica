# Lee cuatro palabras desde teclado e imprime las
# que contengan la letra "r".

for i in range(4):
    cadena = input("Ingresá una palabra: ")
    if "r" in cadena:
        print(cadena)