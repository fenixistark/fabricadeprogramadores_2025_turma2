def exercicio_514():
    s = 0
    quantidade = 0
    while True:
        v = int(input("Digite um numero ou 0 para sair: "))
        if v == 0:
            break
        s = s + v
        quantidade + 1
    print("A soma é: ", s)
    print("A quantidade é: ", quantidade)
    print("A média é: ", s / quantidade)
    exercicio_514()
    