"""
Ejercicio 2: Serie de Fibonacci
Generar los primeros 15 números de la serie de Fibonacci usando ciclos.
"""

fibonacci = [1, ]

for i in range(1, 100):
    if len(fibonacci) < 15:
        if i == 1:
            fibonacci.append(i)
        else:
            anterior = fibonacci[i-1]
            previo = fibonacci[i-2]
            fibonacci.append(anterior + previo)

print(fibonacci)
print(len(fibonacci))