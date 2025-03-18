#Escribe un programa que imprima la tabla de multiplicar de un número dado por el usuario, desde el 1 hasta el 10, utilizando un bucle for.
numero = int(input("Introduce un numero:"))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1,11):
    print(f"{numero} x :{i} = {numero * i} ")