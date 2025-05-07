#Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def numero_par_impar_t_f(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un numero entero: "))

print (numero_par_impar_t_f(numero))