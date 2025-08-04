import time
"""print("iniciando contagem regressiva para o lançamento do foguete!")
x = 10
while x >= 1:
    print(x)
    x = x - 1
print ("fogo")
x = 1
while x <= 100:
    print(x)
    x = x + 1
fim=int(input("60"))
x = 0
while x <= fim:
    print(x)
    x += 1"""
def arvore_de_natal():
    linha = 1
    while linha <= 10:
        coluna = 1
        while coluna <= linha:
            print('🌲', end="")
            coluna = coluna + 1
        print()
        linha = linha + 1
arvore_de_natal()
            