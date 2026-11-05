# Práticas de Python — Unidade 3: Eficiência energética e qualidade de energia

**Base:** Mariani e Silva, *Eficiência energética e qualidade de energia* (2017), Unidade 3.
Os códigos são exercícios didáticos originais relacionados aos assuntos do livro, não reproduções literais dos exercícios.

## Aula 1 — Qualidade da energia (a partir da p. 111)
01. Tensão eficaz a partir de amostras de uma senoide
02. Variação percentual da tensão
03. Tensão em por unidade (pu)
04. Distorção harmônica total de corrente (THD)
05. Gráfico de senoide com harmônicas

## Aula 2 — Falhas no sistema elétrico (a partir da p. 124)
06. Desequilíbrio de tensão (método NEMA, p. 129)
07. Afundamento de tensão
08. Elevação de tensão
09. Duração de distúrbios em ciclos
10. Gráfico de afundamento de tensão

## Aula 3 — Indicadores usados nos sistemas elétricos (a partir da p. 138)
11. DIC: duração de interrupção individual
12. FIC: frequência de interrupção individual
13. DMIC: duração máxima de interrupção contínua
14. DEC: duração equivalente por unidade consumidora (exemplo p. 147)
15. FEC: frequência equivalente por unidade consumidora (exemplo p. 147)

## Como executar

1. Instale Python 3.9 ou superior.
2. No terminal (Windows, Linux ou macOS), entre na pasta de uma das aulas.
3. Execute, por exemplo: `python 01_tensao_eficaz.py` ou `py 01_tensao_eficaz.py` no Windows.
4. Para os dois programas com gráficos, instale antes: `python -m pip install matplotlib`.
5. Substitua os números das variáveis pelos dados dos exercícios propostos em sala.

## Observações importantes

- Dados ilustrativos, salvo o exemplo DEC/FEC de 500 consumidores que reproduz os valores da p. 147.
- A média RMS de uma senoide é calculada sobre amostras igualmente espaçadas de um ciclo completo.
- O THD considera os valores eficazes das harmônicas e a fundamental.
- No código 06, o desequilíbrio é medido pelo **método NEMA**, também descrito no livro. **Não** confundir com o método PRODIST usado em avaliações regulatórias.
- Os indicadores DIC, FIC, DMIC, DEC e FEC usam aqui eventos fictícios já considerados contabilizáveis. Apurações regulatórias exigem filtros, períodos e regras em vigor.
- O livro é de 2017; limites e critérios regulatórios devem ser confrontados com a redação atual aplicável do PRODIST antes de aplicações profissionais.
- Os programas gráficos salvam os arquivos PNG na pasta de trabalho e abrem uma janela de visualização.
