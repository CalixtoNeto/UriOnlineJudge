i = 0
pares = 0
while i < 5:
    n = int(input())
    i += 1
    if n % 2 == 0:
        pares += 1
print("{} valores pares".format(pares))
