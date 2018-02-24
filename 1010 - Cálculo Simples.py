lista1=input().split(" ")
lista2=input().split(" ")

cod1, quant1, valor1 = lista1
cod2, quant2, valor2 = lista2
print('VALOR A PAGAR: R$ {:.2f}'.format(int(quant1)* float(valor1) + int(quant2)* float(valor2)))