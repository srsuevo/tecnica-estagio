#### Faturamento Diário

Este script Python analisa os dados de faturamento diário do arquivo json para encontrar o menor e maior valor e o número de dias acima da média mensal.

### Código

```python
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

### Como executar

Navegue para o diretório calcular_faturamento

Execute o script com python calcularfaturamento.py

### Exemplo de saída


menor faturamento: 1530.98
maior faturamento: 9513.44
dias com faturamento acima da média: 5