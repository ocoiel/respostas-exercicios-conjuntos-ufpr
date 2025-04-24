import csv

def analisar_streaming(arquivo_csv='streaming.csv'):
    series_por_usuario = {}
    
    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            usuario = linha['usuario']
            serie = linha['serie']
            
            if usuario not in series_por_usuario:
                series_por_usuario[usuario] = set()
            
            series_por_usuario[usuario].add(serie)
    
    print("Séries por usuário:")
    for usuario, series in series_por_usuario.items():
        print(f"{usuario}: {series}")
    
    # Séries assistidas por todos os usuários
    usuarios = list(series_por_usuario.keys())
    series_todos = set.intersection(*[series_por_usuario[u] for u in usuarios])
    # *[series_por_usuario[u] for u in usuarios] é equivalente a
    # [series_por_usuario['Ana'], series_por_usuario['Carlos'], ...]
    # ou seja, pega todas as séries de todos os usuários e faz a interseção
    # entre elas
    print("\nSéries assistidas por todos:", series_todos)
    # O resultado esperado é: vazio, pois não há séries assistidas por todos os usuários ao mesmo tempo
    
    # Séries que Ana assistiu mas Carlos não
    if 'Ana' in series_por_usuario and 'Carlos' in series_por_usuario:
        series_ana_nao_carlos = series_por_usuario['Ana'] - series_por_usuario['Carlos']
        print("\nSéries que Ana assistiu mas Carlos não:", series_ana_nao_carlos)
    
    maior_intersecao = 0
    par_similar = None
    
    for i in range(len(usuarios)):
        for j in range(i+1, len(usuarios)):
            usuario1 = usuarios[i]
            usuario2 = usuarios[j]
            
            intersecao = series_por_usuario[usuario1] & series_por_usuario[usuario2]
            if len(intersecao) > maior_intersecao:
                maior_intersecao = len(intersecao)
                par_similar = (usuario1, usuario2)
    
    if par_similar:
        print(f"\nUsuários com gostos mais similares: {par_similar[0]} e {par_similar[1]}")
        print(f"Séries em comum: {series_por_usuario[par_similar[0]] & series_por_usuario[par_similar[1]]}")

analisar_streaming()