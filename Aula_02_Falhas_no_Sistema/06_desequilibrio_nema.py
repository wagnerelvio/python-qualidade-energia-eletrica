"""Exercício 6: desequilíbrio de tensão de linha pelo método NEMA.
O livro também descreve o método PRODIST, que deve ser usado
para verificações regulatórias; o método NEMA é didático.
"""
tensoes = [220.0, 215.0, 225.0]  # V_AB, V_BC, V_CA
media = sum(tensoes) / 3
maior_desvio = max(abs(v - media) for v in tensoes)
indice = 100 * maior_desvio / media
print(f"Média = {media:.2f} V")
print(f"Maior desvio = {maior_desvio:.2f} V")
print(f"Desequilíbrio NEMA = {indice:.2f}%")
