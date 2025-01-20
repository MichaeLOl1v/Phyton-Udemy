# Functions (Funções)
    # Realizam uma tarefa
    # Calcula e retorna um Valor


def cliente1(nome): # A função 1 imprimiu na tela
    print(f'Olá {nome}')


def cliente2(nome): # Na função 2 imprime no programa (para aparecer é encessário que utilize o print)
    return f'Olá {nome}' # Return armazena a informção, que pode ser jogada em uma variavel e imprmir a variavel na tela ou ultilizar em outro calculo ou função

x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)