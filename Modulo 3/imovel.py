from abc import ABC, abstractmethod

class Imovel(ABC): #classe abstrata
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome # CONVENCAO // um underline = metodo protegido // dois underline = metodo privado
        self._uf = uf
        self._valor = valor
        self._endereco = endereco
        self._area = area

    @property  #metodos define propriedade 'getNome'
    def nome(self):
        return self._nome
    
    @nome.setter #metodos define o valor da propriedade 'setNome'
    def nome(self, nome):
        self._nome = nome

    @property
    def uf(self):
        return self._uf
    
    @uf.setter
    def uf(self, uf):
        self._uf = uf 

    def detalhar(self):
        print(self.__dict__)

    def calcularImposto(self):
        return self._valor * 0.02
    
    @abstractmethod #metodo abstrato. Caso nao seja escrtito aluguelSugerido nas classes filhas da erro
    def aluguelSugerido(self):
        ...


class ImovelResidencial(Imovel): #Para herança é só inserir a classe dentro do ()
    def __init__(self, nome, uf, valor, endereco = '', area = ''): #sobrescreveu a classe pai
        super().__init__(nome, uf, valor, endereco = '', area = '') #passar os parametros da superclasse pai
        self._quartos = 0
        self._piscina = False

    def aluguelSugerido(self):
        return self._valor * 0.01

class ImovelComercial(Imovel):
    
    def aluguelSugerido(self):
        return self._valor * 0.02

class ImovelRural:
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self._hectares = hectares
        self._curral = curral
        self._produtiva = produtiva
    
    def mesPlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')
        
class Fazenda(Imovel, ImovelRural):
    def aluguelSugerido(self):
        return self._valor * 0.03


fazenda = Fazenda('Fazenda Modelo', 'GO', 1500000)
clinica = ImovelComercial('Clínica X', 'DF', 800000)
casa = ImovelResidencial('Casa Guará', 'DF', 350000)

casa.nome = 'Casa muito bonita'
casa.uf = 'SP'
casa.detalhar()


# imovel = Imovel('Residencial Aeronautica', 'DF', 400000)
# imovel.endereco = 'QI 23'
# imovel.area = '80'
# imovel.detalhar()