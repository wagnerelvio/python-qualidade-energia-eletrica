"""Exercício 8: amplitude e aumento de tensão em evento de elevação."""
v_ref = 220.0
v_evento = 264.0
v_pu = v_evento / v_ref
aumento = (v_evento - v_ref) / v_ref * 100
print(f"Tensão do evento = {v_evento:.1f} V")
print(f"Tensão relativa = {v_pu:.2f} pu")
print(f"Elevação = {aumento:.1f}%")
