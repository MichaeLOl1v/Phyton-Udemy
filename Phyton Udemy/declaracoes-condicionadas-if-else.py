# if / elseif = elif / else

# Quando estamos viajando numa rodovia e a velocidade permitida é 110kmh, acima desse velocidade "acima da velocidade" ou "dentro do limite" ou "abaixo do minimo permitido"

velocidade = input('Digite a velocidade: ')
velocidade = int(velocidade)

if velocidade > 110:
    print('Acima da velocidade permitida')
    print('Favor reduzir a sua velocidade')

elif velocidade < 70:
    print('Velocidade muito abaixo do permitido, por cima dirigir acima de 80')

else:
    print('Velocidade ok') 