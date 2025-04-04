import json

with open('dados.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

valores_validos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_valor = min(valores_validos)
maior_valor = max(valores_validos)
media_mensal = sum(valores_validos) / len(valores_validos)
dias_acima_media = sum(1 for valor in valores_validos if valor > media_mensal)

print("Resultados da análise de faturamento:")
print(f"1. Menor valor de faturamento: R${menor_valor:.2f}")
print(f"2. Maior valor de faturamento: R${maior_valor:.2f}")
print(f"3. Média mensal de faturamento: R${media_mensal:.2f}")
print(f"4. Dias com faturamento acima da média: {dias_acima_media}")