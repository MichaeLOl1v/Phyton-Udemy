

# Unpacking Lists
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja','banana']

item1, item2, *outros, item8 = produtos

print(item1)
print(item2)
print(item8)
print(outros)