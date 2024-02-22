# Aula 02: TypeError, Type Check, Type Conversion, try-except e if

Bem-vindo à segunda aula do bootcamp!

Hoje, vamos explorar mais a fundo um dos conceitos mais fundamentais da programação: variáveis. As variáveis são essenciais para armazenar e manipular dados em qualquer linguagem de programação, e em Python não é diferente. Nesta aula, vamos entender o que são variáveis, como declará-las, os tipos de dados simples suportados por Python e algumas boas práticas para nomeá-las.

Além disso, vamos mostrar como lidar e trabalhar com erros usando `TypeError`, `Type Check`, `Type Conversion`, `try-except` e `if`.

## 1. Tipos primitivos

Variáveis são espaços de memória designados para armazenar dados que podem ser modificados durante a execução de um programa. Em Python, a declaração de variáveis é dinâmica, o que significa que o tipo de dado é inferido durante a atribuição.

### Exemplo em Python:

Python suporta vários tipos de dados simples, tais como:

- **Inteiros (int)**: Representam números inteiros.
- **Ponto Flutuante (float)**: Representam números reais.
- **Strings (str)**: Representam sequências de caracteres.
- **Booleanos (bool)**: Representam valores verdadeiros (True) ou falsos (False).

#### 1.1 Inteiros (int)

Métodos e operações:
- `+` (adição)
- `-` (subtração)
- `*` (multiplicação)
- `//` (divisão inteira)
- `%` (módulo - resto da divisão)

#### 1.2 Números de Ponto Flutuante (float)

Métodos e operações:
- `+` (adição)
- `-` (subtração)
- `*` (multiplicação)
- `/` (divisão)
- `**` (potenciação)

#### 1.3 Strings (str)

Métodos e operações:
- `.upper()` (converte para maiúsculas)
- `.lower()` (converte para minúsculas)
- `.strip()` (remove espaços em branco no início e no final)
- `.split(sep)` (divide a string em uma lista, utilizando `sep` como delimitador)
- `+` (concatenação de strings)

#### 1.4 Booleanos (bool)

Operações lógicas:
- `and` (E lógico)
- `or` (OU lógico)
- `not` (NÃO lógico)
- `==` (igualdade)
- `!=` (diferença)

## TypeError, Type Check e Type Conversion em Python

Python é uma linguagem de programação dinâmica, mas fortemente tipada, o que significa que não é necessário declarar tipos de variáveis explicitamente, mas o tipo de uma variável é determinado pelo valor que ela armazena. Isso introduz a necessidade de compreender como Python lida com diferentes tipos de dados, especialmente quando se trata de operações que envolvem múltiplos tipos. Vamos explorar três conceitos importantes: TypeError, verificação de tipo (type check), e conversão de tipo (type conversion).

### TypeError

Um TypeError ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

#### Exemplo de TypeError

Um exemplo clássico é tentar utilizar a função len() com um inteiro, o que resulta em TypeError, pois len() espera um objeto iterável, como uma string, lista, ou tupla, não um inteiro.

```python
# Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro