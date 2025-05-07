#Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) 
#para definir el rango de multiplicación. Por defecto es del 1 al 10

def tabla_multiplicar(numero: int, inicio=1, fin=10) -> int:
    for i in range(inicio, fin+1):
        print (f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese su numero: "))
tabla_multiplicar(numero)
