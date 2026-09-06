
compras = []
contador = 1
for x in range(3):
    stuff = input("O que queres adicionar à lista de compras?")
    compras.append(stuff)
print (compras)
for x1 in compras:
    print((contador),". Tenho que comprar", (x1))
    contador = contador + 1   

------------

def par_ou_impar(number):
    if number % 2 > 0:
        print("O número",(number),"é ímpar")
    else:
        print("O número",(number),"é par")

numbers = [4,7,10]
for x in numbers:
    par_ou_impar(x)

-----------

def classificar_nota(nota):
    if nota < 10:
        print((nota),"- Reprovado")
    elif nota < 13:
        print((nota),"- Sufeciente")
    elif nota < 16:
        print((nota),"- Bom")
    else:
        print((nota),"- Muito Bom")

notas = [15,11,3,19,20]
for x in notas:
    classificar_nota(x)

-----------

def soma_lista(numbers):
    return sum(numbers)

numeros = [1,2,3,4,5,6]
result = soma_lista(numeros)
print("A soma é:",(result))

-----------

def soma_lista(numbers):
    contador = 0
    for x in numbers:
        contador = contador + x
    return(contador)
    

numeros = [1,2,3,4,5,6]
result = soma_lista(numeros)
print("A soma é:",(result))

-----------

    numbers = [4,83,2,13,1035,23,68]
    def maior_numero(numeros):
        number = numeros[0]
        for x in numeros:
            if number < x:
                number = x
        return number

    max = maior_numero(numbers)
    print(max)

-----------

carrinho = [
    {"nome": "Ferrari", "preco": 5000},
    {"nome": "Bicicleta", "preco": 150},
    {"nome": "Skate", "preco": 80}
    ]

total = 0
for x in carrinho:
    total = total + x["preco"]
    print(x["nome"],":", x["preco"])
print("A soma é:",total)

-----------

carrinho = [
    {"nome": "Ferrari", "preco": 5000},
    {"nome": "Bicicleta", "preco": 150},
    {"nome": "Skate", "preco": 80}
    ]

def produto_mais_caro(dic):
    mais = dic[0]["preco"]
    nome = dic[0]["nome"]
    for x in dic:
        if x["preco"] > mais:
            mais = x["preco"]
            nome = x["nome"]
    return nome

chama = produto_mais_caro(carrinho)
print("O produto mais caro é:",chama)

-----------

carrinho = [
    {"nome": "Ferrari", "preco": 5000,"quantidade":10},
    {"nome": "Bicicleta", "preco": 150,"quantidade":15},
    {"nome": "Skate", "preco": 80,"quantidade":5},
    {"nome": "Board", "preco": 30,"quantidade":54},   
    ]

def valor_total_stock(dic):
    total = 0
    for x in dic:
       total = total + x["preco"] * x["quantidade"]
    return total

def produto_menos_stock(dic):
    nome = dic[0]["nome"]
    quantidade = dic[0]["quantidade"]
    for x in dic:
        if quantidade > x["quantidade"]:
            quantidade = x["quantidade"]
            nome = x["nome"]
    return nome

def listar_inventario(dic):
    for x in dic:
        valor = x["preco"] * x["quantidade"]
        print(x["nome"],"|","Preço -",x["preco"],"|","Quantidade - ",x["quantidade"],"|","Valor - ",valor)

listar_inventario(carrinho)
toma2 = produto_menos_stock(carrinho)
print("O produto com menos stock é:",toma2)
toma1 = valor_total_stock(carrinho)
print("O valor total do stock é",toma1)

---------

try:
    idade = int(input("Qual é a tua idade?"))
    print("Tens",idade,"anos")

except:
    print("Isso não é um número válido, tenta outra vez")


---------

while True:
    try:
        x = int(input("Quantos anos tens? "))
        print("Tens", x, "anos")
        break
    except ValueError:
        print("Isso não é um número válido, tenta outra vez")

-----------

nome = str(input("Qual o teu nome?"))
print(nome.upper())
print(nome.lower())
print(f"Olá, {nome}! O teu nome tem {len(nome)} letras.")

----------


tripla = input("Escreve 3 frutas separadas por vírgula (ex: maçã,banana,pera)")
lista = tripla.split(",")
for x in lista:
    print(f"Fruta: {x}") 


-----------


