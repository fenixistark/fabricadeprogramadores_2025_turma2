"""L=[9,9,15]
for jão in L:
    print(jão)
L=["CR7", "Neymar", "Messi"]
for s in L:
    for letra in s:
        print(letra)
L=[1,7,2,4]
menor=L[1]
for e in L:
    if e < menor:
        menor = e
        print(menor)
for v in range(11):
    print(v)
for v in range(5, 8):
    print(v)
for t in range(76,3365,334):
    print(t,end=" ")"""
nome = "João"
idade = 15
grana = 435.32
print("%s tem %d anos e R$f no bolso. " % (nome, idade, grana))
print("%12s tem %03d anos e R$5.2f no bolso. " % (nome,idade,grana))
print("%-12s tem %-3d anos e R$%-5.2f no bolso. " % (nome, idade, grana))
