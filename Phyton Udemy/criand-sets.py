
# Set (listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # '|' significa Union = vai unir as listas removendo os numeros repetidos
print(num1 - num2) # Difference 
print(num1 ^ num2) # Symmetric Difference = Ele tira os duplicados no duas listas
print(num1 & num2) # And = Mostra oque está duplicado em ambas listas
print(len(num1)) # len = Mostra o tamanho da lista