#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne

def numero_flotante() ->float:
    numero = float(input("Ingrese un numero: "))
    return numero

print (f"Su numero es {numero_flotante()}: ")
