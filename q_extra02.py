import csv

def analisar_compras(arquivo_csv='compras.csv'):
    produtos_por_cliente = {}
    categorias_por_cliente = {}
    todas_categorias = set()
    
    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            cliente = linha['cliente']
            produto = linha['produto']
            categoria = linha['categoria']
            
            if cliente not in produtos_por_cliente:
                produtos_por_cliente[cliente] = set()
                categorias_por_cliente[cliente] = set()
            
            produtos_por_cliente[cliente].add(produto)
            categorias_por_cliente[cliente].add(categoria)
            todas_categorias.add(categoria)
    
    print("Produtos por cliente:")
    for cliente, produtos in produtos_por_cliente.items():
        print(f"{cliente}: {produtos}")
    
    print("\nCategorias por cliente:")
    for cliente, categorias in categorias_por_cliente.items():
        print(f"{cliente}: {categorias}")
    
    clientes = list(categorias_por_cliente.keys())
    categorias_comuns = set.intersection(*[categorias_por_cliente[c] for c in clientes])
    print("\nCategorias comuns a todos os clientes:", categorias_comuns)
    
    if 'Maria' in produtos_por_cliente:
        produtos_maria = produtos_por_cliente['Maria'].copy()
        for cliente, produtos in produtos_por_cliente.items():
            if cliente != 'Maria':
                produtos_maria -= produtos
        print("\nProdutos exclusivos de Maria:", produtos_maria)
    
    print("\nClientes que compraram em todas as categorias:")
    for cliente, categorias in categorias_por_cliente.items():
        if categorias == todas_categorias:
            print(f"- {cliente}")

analisar_compras()