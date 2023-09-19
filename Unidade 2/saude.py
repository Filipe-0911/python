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

l_pacientes = [p.__dict__ for p in pacientes.values()] #criando lista de pacientes
df_pacientes = pd.DataFrame.from_records(l_pacientes, index = pacientes.keys()) #criando DataFrame (tabela)
df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis = 1) #calculando imc df_pacientes
media = np.mean(df_pacientes['IMC']) #media do imc do df_pacientes
sobrepeso = df_pacientes[df_pacientes['IMC'] > 25] #verificando quantos estao com imc acima de 25
percentual = len(sobrepeso) / len(df_pacientes) * 100 #percentual
ordenada = df_pacientes.sort_values(by='IMC') #ordenando do menor pro maior com pandas

plt.bar(ordenada['nome'], ordenada['IMC'] , label='Paciente', color='green')
plt.title('Peso de cada paciente')
plt.xlabel('Nome')
plt.ylabel('Peso')
plt.show()