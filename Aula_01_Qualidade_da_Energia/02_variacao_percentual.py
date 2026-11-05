"""Exercício 2: desvio percentual de tensão em relação à nominal."""
v_nominal = 220.0
v_medidas = [220, 215, 205, 230, 225]
print(f"Tensão nominal: {v_nominal:.1f} V")
for i, v in enumerate(v_medidas, 1):
    desvio = (v - v_nominal) / v_nominal * 100
    print(f"Leitura {i}: {v:.1f} V | desvio = {desvio:+.2f}%")
# O desvio não determina sozinho a conformidade regulatória.
