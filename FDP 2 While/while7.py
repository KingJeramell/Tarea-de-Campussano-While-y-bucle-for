#Escribe un programa que pida al usuario un número entero positivo y luego imprima todos los números impares
#desde 1 hasta el número ingresado utilizando un bucle while.
numero = int(input("Introduce un numero entero positivo:"))
if numero > 0:
 print(f"numeros impares desde 1 hasta {numero}:")
i = 1
while i <= numero:
 print(i)
 i += 2
else: 
 print("Por favor introduzca un numero entero positivo")