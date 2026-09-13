despesas = []
for x in range(3):
    nome = str(input("Qual é a despesa?"))
    valor = float(input("Qual é o valor da despesa?"))
    categoria = str(input("Que tipo de despesa é?"))
    despesa = {"Nome": nome,"Valor": valor,"Categoria": categoria}
    despesas.append(despesa)

for i in (despesas):
    print(i["Nome"], "-", i["Valor"], "€","(",i["Categoria"],")")

total = 0
for x1 in despesas:
    total = total + x1["Valor"]
print("Total gasto é:",total,"€")

totais_categoria = {}
for x2 in despesas:
    if x2["Categoria"] in totais_categoria:
        totais_categoria[x2["Categoria"]] = totais_categoria[x2["Categoria"]] + x2["Valor"]
    else:
        totais_categoria[x2["Categoria"]] = x2["Valor"]

for categoria in totais_categoria:
    print("Categoria:",categoria,"Valor Total:","|",totais_categoria[categoria],"€")

ficheiro = open("despesas.txt","w")
for x3 in despesas:
    ficheiro.write(x3["Nome"] + " - " + str(x3["Valor"]) + "€ (" + x3["Categoria"] + ")\n")
ficheiro.write("Total:" + str(total) + "€")
ficheiro.close()
