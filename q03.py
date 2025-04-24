alunos = [
    {"nome": "Ana", "notas": {"matemática": 8.5, "português": 9.0, "ciências": 7.5}},
    {"nome": "João", "notas": {"matemática": 7.0, "português": 6.5, "ciências": 8.0}},
    {"nome": "Maria", "notas": {"matemática": 9.5, "português": 8.0, "ciências": 9.0}}
]

# 1. Calcular a média de cada aluno
def calcular_media_aluno(aluno):
    notas = aluno["notas"].values()
    return sum(notas) / len(notas)

for aluno in alunos:
    media = calcular_media_aluno(aluno)
    print(f"Média de {aluno['nome']}: {media:.2f}")

# 2. Encontrar o aluno com a maior média
def encontrar_melhor_aluno(alunos):
    melhor_aluno = None
    maior_media = -1
    
    for aluno in alunos:
        media = calcular_media_aluno(aluno)
        if media > maior_media:
            maior_media = media
            melhor_aluno = aluno
    
    return melhor_aluno, maior_media

melhor_aluno, maior_media = encontrar_melhor_aluno(alunos)
print(f"Melhor aluno: {melhor_aluno['nome']} com média {maior_media:.2f}")

# 3. Identificar disciplina com maior média geral
def encontrar_disciplina_maior_media(alunos):
    somas_disciplinas = {}
    for aluno in alunos:
        for disciplina, nota in aluno["notas"].items():
            if disciplina not in somas_disciplinas:
                somas_disciplinas[disciplina] = {"soma": 0, "count": 0}
            
            somas_disciplinas[disciplina]["soma"] += nota
            somas_disciplinas[disciplina]["count"] += 1
    
    medias_disciplinas = {}
    for disciplina, dados in somas_disciplinas.items():
        medias_disciplinas[disciplina] = dados["soma"] / dados["count"]
    
    return max(medias_disciplinas.items(), key=lambda x: x[1])

melhor_disciplina, media = encontrar_disciplina_maior_media(alunos)
print(f"Disciplina com maior média: {melhor_disciplina} com {media:.2f}")

# 4. Lista ordenada por desempenho
def ordenar_alunos_por_desempenho(alunos):
    return sorted(alunos, key=calcular_media_aluno, reverse=True)

alunos_ordenados = ordenar_alunos_por_desempenho(alunos)
print("Alunos ordenados por desempenho:")
for aluno in alunos_ordenados:
    print(f"{aluno['nome']}: {calcular_media_aluno(aluno):.2f}")
