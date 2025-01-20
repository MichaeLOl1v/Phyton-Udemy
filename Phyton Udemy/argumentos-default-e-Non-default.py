# Functions (Funções)
    # DRY - Dom't repeat yourself.
    # Parametro --> Argumento
    # Default = Aquele que você define o valor no parametro
    # Non-Default = Aquele que você não define o valor no parametro

def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 4) # Se não passar o argumento o parametro irá utilizar ele mesmo (default)

# Contém uma regra, tem uma ordem... o Argumento Non-Default sempre tem que ser primeiro.