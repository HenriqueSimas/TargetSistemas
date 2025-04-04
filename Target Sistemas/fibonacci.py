def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")