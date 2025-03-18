#Escribe un programa que pida al usuario un número entero positivo. 
# El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.
num = int(input("Introduce un numero entero positivo:"))
if num < 0:
    print("El numero debe ser positivo")
else:
    contador = 0
    temp = num
    while temp > 0:
        temp //= 10
        contador += 1

        print:(f"el numero {num} tiene {contador} digitos")