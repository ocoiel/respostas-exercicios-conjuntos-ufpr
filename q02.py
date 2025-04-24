evento_treinamento = {"Ana", "Carlos", "João", "Mariana", "Pedro"}
evento_confraternizacao = {"João", "Mariana", "Lucas", "Pedro", "Camila"}
evento_palestra = {"Ana", "Pedro", "Camila", "Juliana"}
todos_funcionarios = {"Ana", "Carlos", "João", "Mariana", "Pedro", "Lucas", "Camila", "Juliana", "Rafael", "Bianca"}

# 1. Funcionários que participaram de todos os eventos
participaram_todos = evento_treinamento & evento_confraternizacao & evento_palestra
print("Participaram de todos os eventos:", participaram_todos)

# 2. Funcionários que participaram de pelo menos dois eventos
participaram_treinamento_confraternizacao = evento_treinamento & evento_confraternizacao
participaram_treinamento_palestra = evento_treinamento & evento_palestra
participaram_confraternizacao_palestra = evento_confraternizacao & evento_palestra
participaram_pelo_menos_dois = participaram_treinamento_confraternizacao | participaram_treinamento_palestra | participaram_confraternizacao_palestra
print("Participaram de pelo menos dois eventos:", participaram_pelo_menos_dois)

# 3. Funcionários que participaram apenas do treinamento
apenas_treinamento = evento_treinamento - (evento_confraternizacao | evento_palestra)
print("Participaram apenas do treinamento:", apenas_treinamento)

# 4. Funcionários que não participaram de nenhum evento
nenhum_evento = todos_funcionarios - (evento_treinamento | evento_confraternizacao | evento_palestra)
print("Não participaram de nenhum evento:", nenhum_evento)