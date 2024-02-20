# Solicita ao usuário que insira seu nome
nome = input("Digite seu nome: ")

# Solicita ao usuário que insira o valor do seu salário (aceita números decimais)
salario = float(input("Digite o valor do seu salário mensal: "))

# Solicita ao usuário que insira a porcentagem do bônus recebido (aceita números decimais)
bonus_percentual = float(input("Digite o valor percentual do seu bônus: "))

# Calcula o valor do bônus
bonus_valor = 1000 + salario * (bonus_percentual / 100)

# Exibe uma mensagem ao usuário
print(f"Olá {nome}, o seu bônus foi de {bonus_valor:.2f}")
