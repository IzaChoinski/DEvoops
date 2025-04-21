"""Validar se um número é par ou ímpar."""

# Solicita um número ao usuário
numero = input("Digite um número: ")

# Verifica se o input é um número válido
if numero.isdigit() or (numero.startswith('-') and numero[1:].isdigit()):
    numero = int(numero) 
    if numero % 2 == 0:
        print(f"O número {numero} é **par**.") 
    else:
        print(f"O número {numero} é **ímpar**.") 
else:
    print("Entrada inválida. Por favor, digite um número inteiro.")