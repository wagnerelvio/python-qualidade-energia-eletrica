"""Exercício 13: DMIC = maior duração de uma interrupção contínua."""
duracoes_min = [15, 45, 30, 10]
dmic_min = max(duracoes_min, default=0)
print(f"DMIC = {dmic_min:.1f} minutos = {dmic_min / 60:.3f} horas")
