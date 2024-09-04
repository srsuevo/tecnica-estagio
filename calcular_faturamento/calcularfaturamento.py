import json

def calcularfaturamento():
    with open('calcular_faturamento/faturamento.json', 'r') as file:
        faturamentomensal = json.load(file)

    faturamentos = [dia['faturamento'] for dia in faturamentomensal if dia['faturamento'] > 0]

    menorfaturamento = min(faturamentos)
    maiorfaturamento = max(faturamentos)

    mediamensal = sum(faturamentos) / len(faturamentos)

    diasacimadameida = sum(1 for faturamento in faturamentos if faturamento > mediamensal)

    return menorfaturamento, maiorfaturamento, diasacimadameida

menor, maior, diasacima = calcularfaturamento()

print(f'menor faturamento: {menor}')
print(f'maior faturamento: {maior}')
print(f'dias com faturamento acima da média: {diasacima}')