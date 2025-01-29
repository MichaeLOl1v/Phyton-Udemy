
# Listas
    # Armazenar maid de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#                 0                1           2          4        <-- index

# cidades.append('Santa Catarina') # .append -> função para mandar para o final da lista
# cidades.remove('Salvador') # .remove -> Remover um item 
# cidades.insert(1, 'Santa Catarina') # .insert -> Inserir um item na posição desejada (a posição vem primeiro que o item)
# cidades.pop(0) # .pop -> remover um item conforme a posição
cidades.sort() # Organizar os itens em ordem alfabetica

print(cidades)