# Functions (Funções)
    # DRY - Dom't repeat yourself.
    # Vários argumentos (xargs)

# Criar uma função que soma vários números.

def soma(*numeros): # quando é inserido o "*" significa que se pode colocar varios numeros, não tem um, numero definido
    resultado = 0 # A soma será iniciada do 0 por exemplo: 0 + 2 = 2 + 3 = 5 e assim por diante por conta do loop até o numero final
    for num in numeros: # A soma está sendo realizada dentro do ForLoop
        resultado += num # += Significa que ele vai pegar o resultado e vai somar com o numero novamente
    return resultado # Ao somar todos os numeros o valor é retornado


x = soma(2,3,4,7)

print (x)