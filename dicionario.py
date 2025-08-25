"""tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}
print(tabela["Alface"])
print(tabela["Batata"])
print(tabela["Tomate"])
print(tabela["Feijão"]) 
tabela["Cebola"] = 1.20
tabela["Limão"] = 0.30
print(tabela)
print("Manga" in tabela)
print("Alface" in tabela)"""
estoque = {   
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

total = 0
print("=== Registro de Vendas ===")

while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ").lower()
    
    if produto == "fim":
        break
    
    if produto not in estoque:
        print("Produto não encontrado no estoque.")
        continue
    
    try:
        quantidade = int(input("Digite a quantidade vendida: "))
    except ValueError:
        print("Quantidade inválida. Tente novamente.")
        continue
    
    if quantidade > estoque[produto][0]:
        print(f"Estoque insuficiente! Disponível: {estoque[produto][0]}")
        continue
    
    preco = estoque[produto][1]
    custo = preco * quantidade
    estoque[produto][0] -= quantidade
    total += custo
    
    print(f"Venda registrada: {produto} - {quantidade} x R$ {preco:.2f} = R$ {custo:.2f}\n")

print(f"\nCusto total das vendas: R$ {total:.2f}\n")

print("=== Estoque Atualizado ===")
for nome, dados in estoque.items():
    print(f"Descrição: {nome}")
    print(f"Quantidade: {dados[0]}")
    print(f"Preço: R$ {dados[1]:.2f}\n")