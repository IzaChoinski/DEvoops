"""Módulo para verificar se um número é par ou ímpar."""

def verificar_par_ou_impar():
    """Solicita um número ao usuário e informa se é par ou ímpar."""
    numero = input("Digite um número: ")

    if numero.isdigit() or (numero.startswith('-') and numero[1:].isdigit()):
        numero = int(numero)
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    else:
        print("Entrada inválida. Por favor, digite um número inteiro.")


if __name__ == "__main__":
    verificar_par_ou_impar()
