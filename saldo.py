"""saldo = int( input("valor") )
saque = int( input("saque") )

if saldo >= saque:
    saldo -= saque
    print("Você realizou um saque com sucesso.",saldo)
else:
    print("Erro voce não tem saldo o suficiente",saldo)
nome = input("Digite o nome do Aluno")

nota1 = float( input("digite a primeira nota") )
nota2 = float( input("digite a sengunda nota") )
media = (nota1+nota2)/2
if media >= 6 and media <= 7:
    print("o aluno ", nome , "foi Aprovado com a nota", media)
elif media >= 8: 
    print("o aluno ",nome ,"foi Aprovado com louvor com a nota", media)
else: 
    print("o aluno ",nome ,"foi Reprovado com a nota", media)"""
valor_parte = float(input("Insira o valor parte: "))
porcentagem = float(input("Insira o valor da porcentagem: "))
valor_total = valor_parte * (porcentagem/100)
print(valor_total)
if porcentagem <= 0:
    print("insira um numero maior que zero")
else:
    print(valor_total)