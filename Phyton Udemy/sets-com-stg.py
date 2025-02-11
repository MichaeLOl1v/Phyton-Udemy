
# Set (listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

# set4 = set1.union(set2) # vai unir o set1 com o set2 (removendo os duplicados)
# set4 = set1.difference(set3) # Mostra a diferença
# set4 = set1.intersection(set2) # Mostra oque tem tanto no set1 quanto no set2
set4 = set1.symmetric_difference(set3) # retira todos todos os duplicados


print(set4)