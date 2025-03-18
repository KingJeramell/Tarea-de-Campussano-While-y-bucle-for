#Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud mientras la contraseña ingresada sea incorrecta. 
# El programa debe continuar hasta que el usuario ingrese la contraseña correcta. Utiliza una estructura whilepara simular un do while.
Contraseña_correcta = "Secreta"
Contraseña_ingresada = ""
Nombre = "Jeramell"
while True:
    Contraseña_ingresada = input("Introduce la Contraseña:") 
    if Contraseña_ingresada == Contraseña_correcta:
      print(f"Bienvenido {Nombre}")
      break
    else:
       print("Acceso denegado intente de nuevo")