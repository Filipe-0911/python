import pandas as pd
import matplotlib.pyplot as plt

class Investimento:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome        
        self.valor = valor        
        self.taxa = taxa        
        self.periodo = periodo

investimentos = {
    "Investimento 1" : Investimento("Tesouro Direto", 10000, 0.02, 5),
    "Investimento 2" : Investimento("Ações", 10000, 0.05, 3),
    "Investimento 3" : Investimento("Poupança", 10000, 0.01, 10),
    "Investimento 4" : Investimento("CDB", 10000, 0.03, 7),
}

l_investimentos = [i.__dict__ for i in investimentos.values()]

df_investimentos = pd.DataFrame.from_records(l_investimentos, index = investimentos.keys())

df_investimentos['Retorno'] = df_investimentos.apply(lambda l: l.valor * (1 + l.taxa) ** l.periodo, axis=1)
print(df_investimentos)
df_investimentos = df_investimentos.sort_values(by="Retorno", ascending=False)
print(df_investimentos)

df_investimentos.plot(kind = 'bar', y="Retorno")
plt.title("Retorno dos Investimentos")
plt.xlabel("Investimentos")
plt.ylabel("Retorno em Reais")
plt.show()