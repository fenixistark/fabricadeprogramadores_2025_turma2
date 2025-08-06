
n = int(input("tabuada de:"))
fim = int(input("digite o valor final da multiplicação>"))
x = 1
while x <= fim:
    print(f'{n} x {x} = {n * x}')
    x=x*2
quantidade = 0
soma = 0
while True:
    numero = int(input("digite o numero inteiro (0 para sair): "))
    if numero == 0:
        break
quantidade += 1
soma += numero
if quantidade > 0:
    media = soma / quantidade
else:
    media = 0
    print(f"\nQuantidade de numeros digitados: {quantidade}")
    print(f"\nSoma dos numeros: {soma}")
    print(f"\nMedia aritimetica: {media:.2f}")
          
