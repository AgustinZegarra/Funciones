#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_numero_par_impar() -> int:
    numero = int(input("Ingrese un numero entero: "))


    if numero % 2 == 0:
        print ("su numero es par")
    else:
        print("su numero es impar") 
    return numero

verificar_numero_par_impar()