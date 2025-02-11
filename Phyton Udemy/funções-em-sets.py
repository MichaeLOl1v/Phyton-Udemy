
# Set (listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [1, 2, 3, 4, 5, 6] # numero duplicado não aparece
s1 = {1, 2, 3, 4, 5, 6}

s1.add(7) # Pode adicionar um numero (duplicados não aparece no print)
s1.update([8 , 9, 10]) # É possivel adicionar mais de um numero
s1.remove(10) # Remove um numero
s1.discard(9) # A diferença entre o remove e o discard é que o 'remove' não pode remover item que não existe no SET já o 'discard' permite


print(s1)
