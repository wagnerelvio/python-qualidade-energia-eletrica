"""Exercício 10: simulação de afundamento entre 0,10 s e 0,18 s.
Requer: pip install matplotlib
"""
import math
import matplotlib.pyplot as plt

frequencia = 60
v_rms = 220
n = 3000
tempo = [i * 0.30 / (n - 1) for i in range(n)]
tensao = []
for t in tempo:
    fator = 0.6 if 0.10 <= t <= 0.18 else 1.0
    tensao.append(fator * v_rms * math.sqrt(2) * math.sin(2 * math.pi * frequencia * t))
plt.plot(tempo, tensao, label="Tensão instantânea")
plt.axvspan(0.10, 0.18, alpha=0.15, label="Afundamento")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.title("Afundamento de tensão simulado")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_afundamento.png", dpi=150)
plt.show()
