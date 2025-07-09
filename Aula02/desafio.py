### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ").strip()

if not nome_usuario:
    print("Você não digitou um nome.")
elif any(char.isdigit() for char in nome_usuario):
    print("O nome não deve conter números.")
else:
    print(f"Olá, {nome_usuario}!")

    # 2) Solicita ao usuário que digite o valor do seu salário
    try:
        salario = float(input("Digite o valor do seu salário: R$ "))
    except ValueError:
        print("Valor inválido. Digite um número válido para o salário.")
    else:
        # 3) Solicita ao usuário que digite o valor do bônus recebido
        try:
            bonus = float(input("Digite o valor do bônus recebido: R$ "))
        except ValueError:
            print("Valor inválido. Digite um número válido para o bônus.")
        else:
            # 4) Calcule o valor do bônus final
            valor_final = salario + bonus

            # 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
            print(f"{nome_usuario}, seu salário é R$ {salario:.2f} e seu bônus foi de R$ {bonus:.2f}.")
            print(f"Total recebido: R$ {valor_final:.2f}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?