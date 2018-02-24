lista = input()
a , b , c = lista.split(" ")
a = float(a)
b = float(b)
c = float(c)
if a < b:
    temp = a
    a = b
    b = temp
if a < c:
    temp = a
    a = c
    c = temp
if b < c:
    temp = b
    b = c
    c = temp
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:

    if a ** 2 == (b ** 2 + c ** 2):
        print("TRIANGULO RETANGULO")
    if a ** 2 > (b ** 2 + c ** 2):
        print("TRIANGULO OBTUSANGULO")
    if a ** 2 < (b ** 2 + c ** 2):
        print("TRIANGULO ACUTANGULO")
    if a == b and a == c and b == c:
        print("TRIANGULO EQUILATERO")
    else:
        if a == b or a == c or b == c:
            print("TRIANGULO ISOSCELES")
