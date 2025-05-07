#Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como-
#-parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

def numero_primo(numero: int) ->bool:
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def mostrar_numeros_primos(numero_max: int)-> int:
    cantidad_primos = 0

    for numero in range(2, numero_max + 1):
        if numero_primo(numero):
            print(numero)
            cantidad_primos += 1
    return cantidad_primos

numero_max = int(input("Ingrese hasta que numero quiere buscar: "))
cantidad = mostrar_numeros_primos(numero_max)

print (f"La cantidad de numeros encontrados es: {cantidad}")