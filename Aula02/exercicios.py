import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero01 = int(input("Inserir um numero inteiro:"))
numero02 = int(input("Inserir um numero inteiro:"))
soma = numero01 // numero02
print("A soma dos numeros é",numero01 + numero02)

# # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
número = int(input("Digite um número: "))
resto_divisao = número % 5
print("O resultado",resto_divisao)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero01 = int(input("Inserir um numero inteiro:"))
numero02 = int(input("Inserir um numero inteiro:"))
multiplicação = numero01 * numero02
print("A soma dos numeros é",numero01 + numero02)


# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero01 = int(input("Inserir um numero inteiro:"))
numero02 = int(input("Inserir um numero inteiro:"))
resultado = numero01 // numero02
print("O resultado dos numeros é",numero01 // numero02)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero01 = int(input("Inserir um numero inteiro:"))
resultado = numero01 ** 2
print(f"O quadrado de {numero01} é {resultado}")
print("O resultado dos numeros é",numero01 // numero02)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero01 = float(input("Inserir um numero :"))
numero02 = float(input("Inserir um numero :"))
soma = numero01 // numero02
print("A soma dos numeros é",numero01 + numero02)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero01 = float(input("Inserir um numero :"))
numero02 = float(input("Inserir um numero :"))
media = (numero01 + numero02) / 2
print("A Média dos numeros é",media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))

# Calcula a potência
potencia = base ** expoente

# Imprime o resultado
print(f"{base} elevado a {expoente} é igual a {potencia}.")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))

# Converte para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Imprime o resultado
print(f"{celsius}°C é igual a {fahrenheit}°F.")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_circulo = float(input("Digite o raio:"))
area_circulo = math.pi *  raio_circulo ** 2
print(f"{area_circulo:.2f}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite um texto: ")

# Converte a string para maiúsculas
texto_maiusculas = texto.upper()

# Imprime o texto convertido
print("Texto em maiúsculas:", texto_maiusculas)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo: ")

# Converte o nome para minúsculas
nome_minusculas = nome_completo.lower()

# Imprime o nome convertido
print("Nome em minúsculas:", nome_minusculas)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")

# Remove os espaços em branco no início e no final da frase
frase_sem_espacos = frase.strip()

# Imprime a frase sem os espaços em branco
print("Frase sem espaços em branco no início e no final:", frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_do_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 é o : {lista_do_dia_mes_ano[0]}")
print(f"O elemento 2 é o : {lista_do_dia_mes_ano[1]}")
print(f"O elemento 3 é o : {lista_do_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Concatena as duas strings
resultado = string1 + string2

# Imprime o resultado da concatenação
print("A concatenação das strings é:", resultado)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input("Digite a primeira expressão booleana (True/False): ").capitalize()
expressao2 = input("Digite a segunda expressão booleana (True/False): ").capitalize()

# Converte as strings para valores booleanos
valor1 = expressao1 == "True"
valor2 = expressao2 == "True"

# Calcula o resultado da operação AND entre as duas expressões
resultado = valor1 and valor2

# Imprime o resultado
print("O resultado da operação AND é:", resultado)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

valor1 = input("Digite o primeiro valor booleano (True/False): ").capitalize()
valor2 = input("Digite o segundo valor booleano (True/False): ").capitalize()

# Converte as strings para valores booleanos
booleano1 = valor1 == "True"
booleano2 = valor2 == "True"

# Calcula o resultado da operação OR
resultado = booleano1 or booleano2

# Imprime o resultado
print("O resultado da operação OR é:", resultado)
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor = input("Digite um valor booleano (True/False): ").capitalize()

# Converte a string para um valor booleano
booleano = valor == "True"

# Inverte o valor booleano
resultado = not booleano

# Imprime o resultado
print("O valor booleano invertido é:", resultado)
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara se os dois números são iguais
sao_iguais = numero1 == numero2

# Imprime o resultado da comparação
print("Os números são iguais?" , sao_iguais)
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica se os números são diferentes
sao_diferentes = numero1 != numero2

# Imprime o resultado da verificação
print("Os números são diferentes?", sao_diferentes)

# #### try-except e if

# # 21: Conversor de Temperatura
try:
    temp = float(input("Digite a temperatura (ex: 32C, 89F): ")[:-1])
    escala = input("Digite a escala para conversão (C para Celsius, F para Fahrenheit): ").upper()

    if escala == "C":
        convertida = (temp * 9/5) + 32
        print(f"{temp}C é igual a {convertida}F")
    elif escala == "F":
        convertida = (temp - 32) * 5/9
        print(f"{temp}F é igual a {convertida}C")
    else:
            print("Escala não reconhecida.")
except ValueError:
        print("Por favor, digite uma temperatura válida.")

# 22: Verificador de Palíndromo
texto = input("Digite uma palavra ou frase: ").lower().replace(" ", "")
if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

# 23: Calculadora Simples
try:
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        print("Resultado:", num1 + num2)
    elif operacao == "-":
        print("Resultado:", num1 - num2)
    elif operacao == "*":
        print("Resultado:", num1 * num2)
    elif operacao == "/":
        print("Resultado:", num1 / num2)
    else:
        print("Operação não reconhecida.")
except ValueError:
    print("Por favor, digite um número válido.")
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")        

# 24: Classificador de Números
try:
    numero = float(input("Digite um número: "))
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")
except ValueError:
    print("Por favor, digite um número válido.")

# 25: Conversão de Tipo com Validação
entrada = input("Digite um número: ")
try:
    numero = float(entrada)
    print("Número válido:", numero)
except ValueError:
    print("Não é um número válido.")