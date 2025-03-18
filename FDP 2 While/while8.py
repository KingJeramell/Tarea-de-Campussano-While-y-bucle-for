#Escribe un programa que imprima la serie de 
#Fibonacci hasta el enésimo término, donde el valor de n lo ingresa el usuario, utilizando un bucle for.
n = int(input("Introduzca el numero de terminos de la serie  Fibonacci:"))

if n > 0:
    a, b = 0, 1
    print("Serie de fibonacci:")
    for _ in range(n):
        print(a, end= " ")
    a,b = b, a + b
    print()
else:
    print("Por favor, Introduzca un numero entero positivo")