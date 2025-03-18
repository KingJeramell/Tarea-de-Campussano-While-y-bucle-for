#Escribe un programa que pida al usuario que ingrese un número entero positivo. 
#El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno, utilizando un bucle while.
numero = (int(input("Digite un numero que sea positivo:")))
if numero > 0:
    contador = 1
    while contador <= numero:
        print(contador)
        contador += 1
    else:
        print("por favor ingrese un numero entero que sea positivo")