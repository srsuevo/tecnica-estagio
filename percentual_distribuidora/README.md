### Percentual de Faturamento

Este script Python calcula o percentual de representação de cada estado dentro do faturamento total mensal.

### código

```python
def calpercentual(faturamentoestados):
    faturamentototal = sum(faturamentoestados.values())

    for estado, faturamento in faturamentoestados.items():
        percentual = (faturamento / faturamentototal) * 100
        print(f'{estado}: {percentual:.2f}%')


faturamentoestados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "outros": 19849.053
}

calpercentual(faturamentoestados)

### Como executar

Navegue para o diretório percentual_distribuidora

Execute o script com python percentual.py

### Exemplo de Saída

SP: 37.53%
RJ: 20.29%
MG: 16.17%
ES: 15.03%
outros: 10.98%

