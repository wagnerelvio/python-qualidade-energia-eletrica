"""Exercício 1: valor eficaz de amostras de tensão senoidal (RMS)."""
import math

v_pico = 311.13  # V; corresponde aproximadamente a 220 V eficazes
frequencia = 60  # Hz
n_amostras = 1200
amostras = [v_pico * math.sin(2 * math.pi * i / n_amostras)
            for i in range(n_amostras)]  # um ciclo completo
v_eficaz = math.sqrt(sum(v**2 for v in amostras) / n_amostras)
print(f"Tensão de pico: {v_pico:.2f} V")
print(f"Frequência: {frequencia} Hz")
print(f"Tensão eficaz (RMS): {v_eficaz:.2f} V")
