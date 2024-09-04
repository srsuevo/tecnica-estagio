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
