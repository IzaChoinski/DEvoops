"""Contador automático que informa se os números são pares ou ímpares."""

import time

def verificar_par_ou_impar(limite=10, intervalo=1):
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            print(f"{numero} é par.")
        else:
            print(f"{numero} é ímpar.")
        time.sleep(intervalo)

if __name__ == "__main__":
    verificar_par_ou_impar()