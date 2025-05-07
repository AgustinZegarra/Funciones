#Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande

def encontrar_maximo_3_numeros () ->int:
    numero1= int(input("Ingrese el primer numero: "))
    numero2= int(input("Ingrese el segundo numero: "))
    numero3= int(input("Ingrese el tercer numero: "))

    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero2
    else:
        return numero3

print (f"El numero maximo es {encontrar_maximo_3_numeros()}")