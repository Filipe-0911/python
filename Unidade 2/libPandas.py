import pandas as pd

cidades = [
    {'nome' : 'Distrito Federal', 'UF' : 'DF', 'populacao' : 3000000},
    {'nome' : 'Rio de Janeiro', 'UF' : 'RJ', 'populacao' : 5000000},
    {'nome' : 'Recife', 'UF' : 'PE', 'populacao' : 1000000},
    {'nome' : 'Sao Paulo', 'UF' : 'SP', 'populacao' : 12000000},
]

dataFrame = pd.DataFrame(cidades)

ordernada = dataFrame.sort_values(by='populacao', ascending=False) #ascending = true deixa crescente

print(ordernada.head(2)['nome'])