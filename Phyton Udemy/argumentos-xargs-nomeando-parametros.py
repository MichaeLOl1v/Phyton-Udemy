# Functions (Funções)
    # DRY - Dom't repeat yourself.
    # Vários argumentos (xargs) identificando o Parametro.

# Criar uma função que armazena numeros e string (dados)

def agencia(**carro): # Dois "**" significa que pode passar na linha abaixo os parametros (linha 10)
    return carro

print(agencia(marca = 'volkswagem', modelo = 'Gol', cor = 'Branco', motor = 1.0, placa = 'aaa-1234' ))