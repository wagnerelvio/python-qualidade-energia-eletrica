"""Exercício 4: THD de corrente a partir dos valores eficazes."""
import math

fundamental = 20.0  # A RMS
harmonicas = {3: 4.0, 5: 3.0, 7: 2.0}  # ordem: corrente RMS (A)
if fundamental <= 0:
    raise ValueError("A corrente fundamental deve ser positiva")
thd = math.sqrt(sum(i**2 for i in harmonicas.values())) / fundamental * 100
print("Harmônicas (A RMS):", harmonicas)
print(f"THD de corrente: {thd:.2f}%")
