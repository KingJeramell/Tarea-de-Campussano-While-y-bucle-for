#Escribe un programa que pida al usuario un número entero y luego imprima todos los números desde ese número hasta el 0 en orden descendente 
# utilizando un bucle while.
num = int(input("introduce un numero entero:"))
while num >= 0:
    print(num)
    num -=1