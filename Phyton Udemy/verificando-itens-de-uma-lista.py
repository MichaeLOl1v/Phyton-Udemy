

# Lista
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:   #.lower input em letra minusculo (cor digitada pelo cliente)
    print('Cor disponivel em estoque')
else:
    print('Cor não disponivel em estoque')