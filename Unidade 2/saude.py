import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

pacientes = {
    "Paciente 1" : Paciente('Jacqueline', 52, 'Feminino', 110, 1.63),
    "Paciente 2" : Paciente('Filipe', 29, 'Masculino', 100, 1.80),
    "Paciente 3" : Paciente('Ianca', 27, 'Feminino', 68, 1.65),
    "Paciente 4" : Paciente('Lemoel', 55, 'Masculino', 110, 1.83),
}

#criando lista de pacientes
l_pacientes = [p.__dict__ for p in pacientes.values()]

#criando DataFrame (tabela)
df_pacientes = pd.DataFrame.from_records(l_pacientes, index = pacientes.keys())

#calculando imc df_pacientes axis = 1 significa a partir do eixo 1
df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis = 1)

#media do imc do df_pacientes
media = np.mean(df_pacientes['IMC'])

#verificando quantos estao com imc acima de 25
sobrepeso = df_pacientes[df_pacientes['IMC'] > 25]

#percentual
percentual = len(sobrepeso) / len(df_pacientes) * 100

#ordenando do menor pro maior com pandas
ordenada = df_pacientes.sort_values(by='IMC') 

plt.bar(ordenada['nome'], ordenada['IMC'] , label='Paciente', color='green')
plt.title('Peso de cada paciente')
plt.xlabel('Nome')
plt.ylabel('Peso')
plt.show()