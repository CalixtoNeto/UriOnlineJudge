lista = input()
id , quant = lista.split(" ")
id = int(id)
quant = float(quant)

if id == 1:
    preco = 4.00
elif id == 2:
    preco = 4.50
elif id == 3:
    preco = 5.00
elif id == 4:
    preco = 2.00
elif id == 5:
    preco = 1.50

print("Total: R$ {:.2f}".format(quant * preco))