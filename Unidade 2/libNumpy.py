import numpy as np

numeros = [1, 2, 3, 4, 5, 6, 7, 8 ]

soma = 0

for n in numeros:
    soma += n


print(soma)

media = soma / len(numeros)
print(f"media feita na mão, ", media)

array_numeros = np.array(numeros)

media = np.mean(array_numeros)
print(f"media feita numpy, ", media)