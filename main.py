from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaDestino, moedaOrigem, valor)
