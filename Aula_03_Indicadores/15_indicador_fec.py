"""Exercício 15: FEC de conjunto, ponderado por consumidores afetados.
Exemplo do livro: 500 consumidores; dois trechos com interrupções.
"""
consumidores_total = 500
eventos = [(200, 5), (300, 15)]  # (consumidores afetados, minutos)
assert all(0 <= n <= consumidores_total and minutos >= 0 for n, minutos in eventos)
fec = sum(n for n, _ in eventos) / consumidores_total
print(f"FEC = {fec:.2f} interrupções/consumidor")
