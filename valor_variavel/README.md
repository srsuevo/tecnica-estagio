### Programa de Soma de Números

Este script em Python calcula a soma dos números de 1 até um índice especificado. O índice é um valor inteiro que define até qual número a soma será calculada.

### Descrição

O programa inicializa três variáveis: `indice`, `soma`, e `k`. Ele então itera de 1 até o valor do `indice`, somando cada valor de `k` à variável `soma`. No final, o valor total da soma é exibido.

### Código

```python
indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)


### Como Executar

Navegue para o diretório valor_variavel
Execute o script com python valorsoma.py

###  Exemplo de Saída

Para o valor de indice igual a 13, a saída será:

91

### Explicação do código


Variáveis:

indice: O valor até o qual a soma será calculada (neste caso, 13).

soma: Armazena a soma dos números.

k: Contador que será incrementado a cada iteração do loop.

Loop: O loop while continua executando enquanto k for menor que indice.

Em cada iteração, k é incrementado em 1 e adicionado à variável soma.

Saída: Após o término do loop, o valor de soma é impresso, que representa a soma de todos os números de 1 até o indice.

Isso porque a soma dos números de 1 a 13 é 91.