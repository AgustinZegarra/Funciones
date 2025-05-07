#Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def potencia_numero(base :float, exponente: float) -> float:

    calculo_potencia = base ** exponente
    return calculo_potencia

base = float(input("Ingrese su numero: "))
exponente = float(input("Ingrese su exponente: "))

print (potencia_numero(base,exponente))