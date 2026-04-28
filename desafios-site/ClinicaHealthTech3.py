consulta = input("digite o seu sintoma: ")


if consulta == ("dor de cabeca"):
    print("repouso em casa")
elif consulta in ["dor no peito", "falta de ar"]:
    print("atendimento imediato")
elif consulta == ("febre"):
    print("agendar consulta")
else:
    print("Sintoma não registrado")
