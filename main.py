from ExtratorArgumentosUrl import ExtratorArgumentosUrl

# Vídeo 01 - None, empty e o if do Python

string = None
print(string is None)

string = ''
print(string is None)

if string:
    print('Tem algo Aqui')
else:
    print('Não tem nada Aqui!!')

string = 'Rogrigo'

if string:
    print('Tem algo Aqui')
else:
    print('Não tem nada Aqui!!')

string = 12

if string:
    print('Tem algo Aqui')
else:
    print('Não tem nada Aqui!!')

string = 0

if string:
    print('Tem algo Aqui')
else:
    print('Não tem nada Aqui!!')

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
argumento = ExtratorArgumentosUrl.urlEhValida(url) 

print(argumento)

url = None
argumento = ExtratorArgumentosUrl.urlEhValida(url) 

print(argumento)

# Vídeo 03 - Construindo mais métodos

"""
Método na classe ExtratorArgumentos, feito no vídeo 03:

        def extraiArgumentos(self):
        
        indiceInicialMoedaDestino = self.url.find('=', 15) + 1

        indiceInicialMoedaOrigem = self.url.find('=') + 1
        indiceFinalMoedaOrigem = self.url.find('&')

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigem, moedaDestino
"""
url = "moedaorigem=real&moedadestino=dolar"

argumentoUrl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentoUrl.extraiArgumentos()
print(moedaOrigem, moedaDestino)

# Vídeo 04 - O método len

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar"

index = url.find('moedadestino') + len('moedadestino') + 1
substring = url[index:]
print(substring)