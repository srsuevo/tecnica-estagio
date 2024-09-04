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