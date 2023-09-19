import matplotlib.pyplot as plt #biblioteca para gerar graficos

# meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
# AIM1 = [60, 52, 26, 32, 64, 32]
# AIM2 = [45, 70, 50, 37, 47, 43]

# plt.plot(meses, AIM1, label = 'AIM1', color = 'blue', linestyle='--', marker='.') #plot sao riscos, bar eh para graficos em barras
# plt.plot(meses, AIM2, label = 'AIM2', color = 'green', linestyle='--', marker='.')
# plt.title('SDIAS tratados')
# plt.xlabel('Meses')
# plt.ylabel('Quantidade')
# plt.legend()


navegadores = ['Chrome', 'Firefox', 'Edge']
quantidade = [1200, 600, 200]
cores = ['red', 'orange', 'blue']

plt.pie(quantidade, labels = navegadores, colors = cores)
plt.show()