# Dentro do if/elif/else pode ser colocados multiplos operadores ('operadores-de-comparação)

# Regras do site. O produto deve ser maior que 20 e menor que 40, menor que 20 e maior que 40 não são aprovados

valor = input('Digite o valor do produto: ')
valor = int(valor)

# if 20 <= valor < 40: (Mesma coisa que a linha abaixo com o código mais limpo)

if valor >= 20 and valor < 40:
    print('Produto aceito para publicação')
else:
    print('Produto não aceito')