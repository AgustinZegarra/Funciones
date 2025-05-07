#Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def numero_entero() ->int:
    numero = int(input("Ingrese un numero entero: "))
    return numero

print (f"Su numero es {numero_entero()}: ")
