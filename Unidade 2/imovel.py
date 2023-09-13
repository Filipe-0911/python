import data

class Categoria:
    def __init__(self, tipo = ''):
        self.tipo = tipo
    
    def taxaAgua(self, consumo):

        print("Data da leitura: ", data.formatarData())

        match self.tipo:
            case 'Clínica' : return consumo * 1
            case 'Restaurante' : return consumo * 2
            case 'Hotel' : return consumo * 2.5

class Imovel:

    imposto = 0.2     #atributo de classe

    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        self.categoria = Categoria() #Metodo de Composicao != de Heranca

    def detalhar(self):
        print(self.__dict__)

    def somarAposentos(self):
        return self.quartos + self.suites

    def __add__(self, other):         #metodos especiais add = soma
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites

        return somaSelf + somaOther
    
    def __gt__(self, other):   #gt e lt retorna < ou > que ...  
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites

        return somaSelf < somaOther
    
    def __lt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites

        return somaSelf > somaOther
    
    def __str__(self):   #str permite que digite print(Object)
        return str(self.__dict__)
    
    def __eq__(self, other):        #__eq__ compara igualdade entre dois objetos
        if isinstance(other, Imovel):
            return self.quartos == other.quartos
        return False
    
    @staticmethod
    def metodoEstatico():
        print('Chamou o metodo estatico sem criar objeto')
    
    @classmethod
    def metodoDeClasse(cls):  #cls = objeto da classe para ver os atributos de classe
        print('Chamou metodo de classe que ve o imposto =', cls.imposto)


apartamento = Imovel('Ap Guará', 3, 1)
mansao = Imovel('Mansao', 4, 5)

categoria = Categoria('Hotel')
hotel = Imovel('Hotel 1 lugar', 0, 150)
hotel.categoria = categoria
print(hotel.categoria.taxaAgua(300))

soma = apartamento + mansao
# print(soma)
# print(mansao > apartamento)
# print(mansao < apartamento)
# print(apartamento)
# print(apartamento == mansao)

# print(mansao.somarAposentos())
# print(apartamento.somarAposentos())

Imovel.metodoEstatico()
print(apartamento.detalhar())
Imovel.metodoDeClasse()

#__len__ retorna a length do objeto (Quantidade)