# Simular uma loja que vende produtos para terceiros (regra o produto tem uma comissão de 10%, caso o produto custe mais de 20 reais)
# While = enquanto

valor = int(input('Digite o valor do seu Produto em R$: '))

while valor > 20:
    valor = (valor * 0.10) + valor  # <--- Acrescentada a comissão de 10%
    print(f'O valor final do seu produto será de R${valor}') # f'= Formata de STRING
    break # Impedir que entre em um loop infinito (As vezes o 'BREAK' é necessário)

