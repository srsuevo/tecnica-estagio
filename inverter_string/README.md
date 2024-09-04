### Inversão de String

Este script Python inverte os caracteres de uma string fornecida pelo usuário.

### Código

```python
def inverterstring(y):
    resultado = ''

    for i in range(len(y) -1, -1, -1):
        resultado += y[i]

    return resultado

texto = input('digite um texto (string) para inverter: ')

inverter = inverterstring(texto)

print(f'o texto (string) invertido é: {inverter}')

### Como Executar

Navegue para o diretório inverter_string.

Execute o script com python inverter.py.

Siga as instruções para inserir um (texto) string e obter o resultado invertido.

### Exemplo de saída

digite um texto (string) para inverter: vaga

o texto (string) invertido é: agva



