# Exercício 01
# print([int(x)**2 for x in input("Entre com os números separados por espaço: ").split()])
# Exercício 02
# print([x if x >= 10 else 0 for x in [int(i) for i in input("Entre com os números separados por espaço: ").split()]])
# Exercício 03
# print([len(x.split()) for x in input("Entre com a sua história: ").split(". ")])
# Exercício 04
# print([sum(1 for c in texto if c.lower() in "aáâãàeêéèiîíìoôóõòuúûù") for texto in ["Frase um", "Frase dois", "Frase três"]])
# Exercício 05
maioresDeIdade = lambda lista:list(filter(lambda x:x["idade"]>=18,lista))
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
print(maioresDeIdade(pessoas))
