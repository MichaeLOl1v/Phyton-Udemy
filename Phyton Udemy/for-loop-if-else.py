# if/elif/else dentro do for loop

# Loja online que quer enviar um email para os clientes os dados(informações) da compra, só que para enviar o email a compra tem que ser realizada

# Break quando entra no FOR LOOP ele verifica se a compra foi confirmada se sim ele imprime e para, caso não ele não sair e retorna para o loop

compra_confirmada = False
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break
else:
    print('Falha na compra')

