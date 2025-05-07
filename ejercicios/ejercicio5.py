#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área

def calculo_area_circulo() -> float:
    pedir_radio_circulo = float(input("Ingrese el radio de su circulo: "))
    area_circulo = 3.14159 * (pedir_radio_circulo * pedir_radio_circulo)
    return area_circulo

print(f"El area de su circulo es: {calculo_area_circulo()} cm²")