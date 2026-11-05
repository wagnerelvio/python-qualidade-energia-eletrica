"""Exercício 11: DIC individual = soma de durações de interrupções.
Dados fictícios de interrupções contabilizáveis em minutos.
"""
duracoes_min = [15, 45, 30, 10]
dic_horas = sum(duracoes_min) / 60
print(f"DIC = {dic_horas:.4f} horas no período")
