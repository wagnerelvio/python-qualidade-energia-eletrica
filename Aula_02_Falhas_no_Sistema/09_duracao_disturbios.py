"""Exercício 9: calcular duração dos distúrbios em ciclos de 60 Hz."""
frequencia = 60.0
eventos = {"Evento A": 0.05, "Evento B": 0.20, "Evento C": 1.50}
periodo = 1 / frequencia
print(f"Período de um ciclo: {periodo * 1000:.3f} ms")
for nome, duracao in eventos.items():
    ciclos = duracao * frequencia
    print(f"{nome}: {duracao:.3f} s = {ciclos:.1f} ciclos")
