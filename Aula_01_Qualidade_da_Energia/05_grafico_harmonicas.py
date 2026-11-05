"""Exercício 5: gráfico de onda com fundamental e harmônicas.
Requer: pip install matplotlib
"""
import math
import matplotlib.pyplot as plt

f = 60.0
amplitude_fundamental = 1.0
n = 1200
t = [i / (f * 2 * (n - 1)) for i in range(n)]  # 2 ciclos
fundamental = [amplitude_fundamental * math.sin(2 * math.pi * f * x) for x in t]
distorcida = [math.sin(2 * math.pi * f * x)
              + 0.20 * math.sin(2 * math.pi * 3 * f * x)
              + 0.10 * math.sin(2 * math.pi * 5 * f * x) for x in t]
plt.plot(t, fundamental, label="Fundamental (60 Hz)")
plt.plot(t, distorcida, label="Com 3ª e 5ª harmônicas")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude normalizada")
plt.title("Efeito de harmônicas na forma de onda")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_harmonicas.png", dpi=150)
plt.show()
