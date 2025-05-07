#Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área

def calculo_area_rectangulo() -> float:
    pedir_base_rectangulo = float(input("Ingrese la base de su rectangulo: "))
    pedir_altura_rectangulo = float(input("Ingrese la altura de su rectangulo: "))
    area_rectangulo = pedir_altura_rectangulo * pedir_base_rectangulo
    return area_rectangulo

print(f"El area de su rectangulo es: {calculo_area_rectangulo()} cm²")