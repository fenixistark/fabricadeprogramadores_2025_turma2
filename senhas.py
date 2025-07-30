minha_senha = "123456"
def verificar_senha(nova_senha):
    if (nova_senha)==(verificar_senha):
        print("valida")
    else:
        print("invalida")
import math
def equação():
    a = float(input("insira o valor de A: "))
    b = float(input("insira o valor de B: "))
    c = float(input("insira o valor de C: "))
    delta = b**2 - 4 * a * c
    if delta >= 0:
        raiz1 = (-b + math.sqrt(delta)) / 2 * a
        raiz2 = (-b - math.sqrt(delta)) / 2 * a
        print("as raizes reais são ",raiz1, raiz2)
    else:
        print("""essa equação não possui raizes reais""")
#equação()
import random
animais = ('lontra', 'lobo', 'gato', 'cachorro', 'vaca', 'cavalo', 'porco', 'galinha', 'rato', 'sapo')
print(random.choice(animais))
import this

