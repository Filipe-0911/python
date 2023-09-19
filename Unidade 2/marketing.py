import matplotlib.pyplot as plt

class Campanha:
    def __init__(self, canal, investimento, cliques, conversoes):
        self.canal = canal
        self.investimento = investimento
        self.cliques = cliques
        self.conversoes = conversoes

    #custo por clique
    def cpc(self):
        return self.investimento / self.cliques

campanhas = [
    Campanha(input("Informe o Canal: "), int(input("Informe o valor investido: ")), int(input("Informe a quantidade de cliques: ")), int(input("Informe a conversão: "))),
    Campanha(input("Informe o Canal: "), int(input("Informe o valor investido: ")), int(input("Informe a quantidade de cliques: ")), int(input("Informe a conversão: "))),
    Campanha(input("Informe o Canal: "), int(input("Informe o valor investido: ")), int(input("Informe a quantidade de cliques: ")), int(input("Informe a conversão: "))),
    Campanha(input("Informe o Canal: "), int(input("Informe o valor investido: ")), int(input("Informe a quantidade de cliques: ")), int(input("Informe a conversão: "))),
]

canais = [c.canal for c in campanhas]
cpcs = [c.cpc() for c in campanhas]

print(canais)
print(cpcs)

plt.bar(canais, cpcs)
plt.title("Custos por Clique")
plt.xlabel("Canais")
plt.ylabel("Custo em Reais")
plt.show()
    

# Campanha('Facebook Ads', 1000, 15000, 150),
# Campanha('Google Ads', 1200, 10000, 200),
# Campanha('Email Ads', 5000, 5000, 50),
# Campanha('Instagram Ads', 800, 12000, 80),