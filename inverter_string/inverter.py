def inverterstring(y):
    resultado = ''

    for i in range(len(y) -1, -1, -1):
        resultado += y[i]

    return resultado

texto = input('digite um texto (string) para inverter: ')

inverter = inverterstring(texto)

print(f'o texto (string) invertida é: {inverter}')