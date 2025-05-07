#Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.

def ingresar_cadena() -> str:
    cadena = input("Ingrese una cadena: ")
    return cadena


print(f"La cadena ingresada es: {ingresar_cadena()}")