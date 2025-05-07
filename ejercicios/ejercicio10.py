#Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario

def numero_primo(numero: int) ->bool:
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un numero entero: "))

print(numero_primo(numero))