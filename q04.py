estoque = {
    "eletrônicos": [
        {"nome": "Smartphone", "preço": 1200, "quantidade": 15},
        {"nome": "Notebook", "preço": 3500, "quantidade": 8}
    ],
    "alimentos": [
        {"nome": "Arroz", "preço": 20, "quantidade": 50},
        {"nome": "Feijão", "preço": 8, "quantidade": 35}
    ]
}

# 1. Calcular o valor total do estoque por categoria
def calcular_valor_por_categoria(estoque):
    valores = {}
    for categoria, produtos in estoque.items():
        valor_total = sum(produto["preço"] * produto["quantidade"] for produto in produtos)
        valores[categoria] = valor_total
    return valores

valores_categorias = calcular_valor_por_categoria(estoque)
for categoria, valor in valores_categorias.items():
    print(f"Valor total de {categoria}: R${valor:.2f}")

# 2. Identificar produtos com estoque abaixo do limite
def produtos_abaixo_limite(estoque, limite):
    produtos_baixos = []
    for categoria, produtos in estoque.items():
        for produto in produtos:
            if produto["quantidade"] < limite:
                produtos_baixos.append({**produto, "categoria": categoria})
    return produtos_baixos

produtos_em_baixa = produtos_abaixo_limite(estoque, 10)
print("Produtos com estoque baixo:")
for produto in produtos_em_baixa:
    print(f"{produto['nome']} ({produto['categoria']}): {produto['quantidade']} unidades")

# OBS.: **produto equivale a produto.copy() + {"categoria": categoria}
# ou seja, cria uma cópia do dicionário produto e adiciona a chave "categoria"
# novo_produto = produto.copy()
# novo_produto["categoria"] = categoria
# produtos_baixos.append(novo_produto)

# 3. Aplicar desconto em uma categoria
def aplicar_desconto(estoque, categoria, percentual):
    if categoria not in estoque:
        return False
    
    for produto in estoque[categoria]:
        produto["preço"] = produto["preço"] * (1 - percentual/100)
    
    return True

aplicar_desconto(estoque, "eletrônicos", 10)
print("Preços após desconto:")
for produto in estoque["eletrônicos"]:
    print(f"{produto['nome']}: R${produto['preço']:.2f}")

# 4. Listar os 3 produtos mais valiosos
def produtos_mais_valiosos(estoque, limite=3):
    todos_produtos = []
    for categoria, produtos in estoque.items():
        for produto in produtos:
            valor_total = produto["preço"] * produto["quantidade"]
            todos_produtos.append({
                "nome": produto["nome"],
                "categoria": categoria,
                "valor_total": valor_total
            })
    
    return sorted(todos_produtos, key=lambda p: p["valor_total"], reverse=True)[:limite]

mais_valiosos = produtos_mais_valiosos(estoque)
print("Produtos mais valiosos:")  
for i, produto in enumerate(mais_valiosos, 1):
    print(f"{i}. {produto['nome']} ({produto['categoria']}): R${produto['valor_total']:.2f}")
