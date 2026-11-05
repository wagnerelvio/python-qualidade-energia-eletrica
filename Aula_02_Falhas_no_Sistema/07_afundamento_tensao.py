"""Exercício 7: amplitude e redução de tensão em um afundamento."""
v_ref = 220.0
v_durante = 154.0
duracao_s = 0.20
v_pu = v_durante / v_ref
queda_percentual = (1 - v_pu) * 100
print(f"Tensão durante o evento = {v_pu:.2f} pu")
print(f"Redução em relação à referência = {queda_percentual:.1f}%")
print(f"Duração informada = {duracao_s:.3f} s")
# Exemplo de afundamento; a classificação temporal depende do critério adotado.
