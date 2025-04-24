frutas_tropicais = {"banana", "manga", "abacaxi", "coco"}
frutas_vermelhas = {"morango", "cereja", "maçã", "manga"}

# 1. União (todas as frutas que aparecem em pelo menos um dos conjuntos)
todas_frutas = frutas_tropicais | frutas_vermelhas
print("União:", todas_frutas)

# 2. Interseção (frutas que aparecem em ambos os conjuntos)
frutas_comuns = frutas_tropicais & frutas_vermelhas
print("Interseção:", frutas_comuns)

# 3. Diferença (frutas exclusivas de frutas_tropicais)
frutas_exclusivas_tropicais = frutas_tropicais - frutas_vermelhas
print("Diferença (exclusivas de tropicais):", frutas_exclusivas_tropicais)

# 4. Diferença simétrica (frutas que aparecem em apenas um dos conjuntos)
frutas_exclusivas = frutas_tropicais ^ frutas_vermelhas
print("Diferença simétrica:", frutas_exclusivas)