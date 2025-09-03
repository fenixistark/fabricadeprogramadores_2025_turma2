tupla = ("data de nascimento", "cpf", "cor dos olhos")
print(tupla)
L=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for x, e in enumerate(L):
    print("[%d] %d" % (x,e))
    print("[%d] X %d = %d" % (x,e, x*e)) #multiplicação
    print("[%d] + %d = %d" % (x,e, x+e)) #adição
    print("[%d] - %d = %d" % (x,e, x-e)) #subtração
    print("[%d] / %d = %d" % (x,e, x/e)) #divisão