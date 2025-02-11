from array import array  # IMPORTANDO UMA ARRAY

# Array (Matriz)
    # Similar a listas
    # Melhor Performance

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd']) # convertendo a lista para array / 'u' array de string
numeros_i = array('i', [10, 20, 30, 40]) # 'i' convertido para integer
numeros_f = array('f', [1.2, 2.2, 3.2]) 

print(letras)
print(numeros_i)
print(numeros_f)

# OBS: TOMAR CUIDADO PARA NÃO PUXAR UMA ARRAY E INFORMAR UM TYPECODE ERRADO