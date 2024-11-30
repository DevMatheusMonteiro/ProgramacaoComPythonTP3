# Exercício 01
# print([int(x)**2 for x in input("Entre com os números separados por espaço: ").split()])
# Exercício 02
# print([x if x >= 10 else 0 for x in [int(i) for i in input("Entre com os números separados por espaço: ").split()]])
# Exercício 03
# print([len(x.split()) for x in input("Entre com a sua história: ").split(". ")])
# Exercício 04
# print([sum(1 for c in texto if c.lower() in "aáâãàeêéèiîíìoôóõòuúûù") for texto in ["Frase um", "Frase dois", "Frase três"]])
# Exercício 05
""" maioresDeIdade = lambda lista:list(filter(lambda x:x["idade"]>=18,lista))
pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 17},
    {"nome": "Pedro", "idade": 34},
    {"nome": "Ana", "idade": 16},
    {"nome": "Lucas", "idade": 18},
    {"nome": "Clara", "idade": 15},
    {"nome": "Gabriel", "idade": 22},
    {"nome": "Bianca", "idade": 14}
]
print(maioresDeIdade(pessoas)) """
# Exercício 06
""" def removerPalavrasIndesejadas(texto, palavrasIndesejadas):
    return " ".join([palavra for palavra in texto.split() if palavra.lower() not in palavrasIndesejadas])
texto = "O melhor time do Rio é o Flamengo, Vasco, Botafogo, Fluminense"
indesejadas = ["vasco","vasco,",", vasco",". vasco","vasco.","botafogo", ", botafogo", "botafogo,","botafogo.", ", fluminense", "fluminense,","fluminense.", ". fluminense","fluminense"]
print(removerPalavrasIndesejadas(texto, indesejadas)) """
# Exercício 07
""" def alternarMaiusculaEMinuscula(texto):
    return "".join(letra.upper() if i % 2 == 0 else letra.lower() for i, letra in enumerate(texto))
texto = "desenvolvendo habilidades, desenvolvendo habilidades"
print(alternarMaiusculaEMinuscula(texto)) """
# Exercício 08
""" def retornarElementosUnicos(matriz):
    return set(i for j in matriz for i in j)
lista = [[2,4,6], [4, 5, 1, 6], [2, 2, 6]]
print(retornarElementosUnicos(lista)) """
# Exercício 09
def intercalarListas(lista1, lista2):
    return [palavra for tupla in zip(lista1, lista2) for palavra in tupla] + lista1[len(lista2):] + lista2[len(lista1):]
lista1 = ["maçã", "banana", "cereja"]
lista2 = ["uva", "laranja", "abacate","limão","abacaxi"]
print(intercalarListas(lista1, lista2))
