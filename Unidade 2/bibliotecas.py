import math
import random #numeros aleatorios
import numpy as np

numero = 6.9
numero = round(numero, 2) #round arredonda o numero

print(numero)
print(math.floor(numero)) #arredonda sempre pra baixo
print(math.ceil(numero)) #arredonda sempre pra cima
print(math.pi)

print(round(random.random() * 100)) #gera numeros aleatorios inteiros devido ao round
print(random.randint(1, 20)) #gera numeros aleatorios inteiros

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)