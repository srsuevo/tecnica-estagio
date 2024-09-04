# Sequência de Fibonacci

Este script Python verifica se um número fornecido pertence à sequência de Fibonacci.

## Código

```python
def sequencia_fibonacci(numero):
    a = 0
    b = 1
    while a <= numero:
        if a == numero:
            return f"o numero {numero} pertence a sequencia fibonacci."
        a, b = b, a + b
    return f"o numero {numero} não pertence a sequencia fibonacci."

numerodigitado = int(input('Digite um número: '))
resultado = sequencia_fibonacci(numerodigitado)
print(resultado)  


### Como executar

Navegue para o diretório sequencia_fibonacci
Execute o script com python sequenciafibonacci.py
Insira um número para verificar se ele pertence à sequência de Fibonacci.

### Exemplo de saída
Digite um número: 21
o numero 21 pertence a sequencia fibanacci.