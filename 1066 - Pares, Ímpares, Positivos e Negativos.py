i = 0
par = 0
impar = 0
pos = 0
neg = 0
while i < 5:
    n = int(input())
    i += 1
    if n % 2 == 0:
        par += 1
    if n % 2 != 0:
        impar += 1
    if n > 0:
        pos += 1
    if n < 0:
        neg += 1

print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(par,
                                                                                                                impar,
                                                                                                                pos,
                                                                                                                neg))

