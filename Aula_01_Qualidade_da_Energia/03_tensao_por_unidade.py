"""Exercício 3: tensão por unidade (pu) e porcentagem da referência."""
v_base = 13800.0  # V
medicoes = [13800, 13200, 14500, 12500]
for v in medicoes:
    pu = v / v_base
    print(f"Tensão: {v:8.0f} V | {pu:.4f} pu | {pu * 100:.2f}% da base")
