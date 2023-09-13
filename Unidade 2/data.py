from datetime import datetime

dataPadraoBr = '%d/%m/%y'
dataPadraoEUA = '%Y-%m-%d'

def formatarData(data = datetime.now(), formato = dataPadraoBr):
    # data = datetime(data)
    return datetime.strftime(data, formato) #padrao BR de data

def criarData(data = datetime.now(), formato = dataPadraoEUA):
    return datetime.strptime(data, formato)
