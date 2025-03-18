#Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while. 
# El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
numero = (int(input("Digite un numero que sea positivo:")))
if numero >= 0:
    factorial = 1
    i = 1
    while i <= numero:
        factorial *= i
        i += 1
        print(f"El factorial del {numero} es {factorial} ")
    else:
        print("Por favor, introduzca otro numero que sea positivo")