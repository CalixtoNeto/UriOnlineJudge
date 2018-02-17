lista = input()
A, B, C = lista.split(" ")
A = int(A)
B = int(B)
C = int(C)

X = A
Y = B
Z = C

if X > Y:
    temp = X
    X = Y
    Y = temp
if X > Z:
    temp = X
    X = Z
    Z = temp
if Y > Z:
    temp = Y
    Y = Z
    Z = temp

print("{}\n{}\n{}\n".format(X,Y,Z))
print("{}\n{}\n{}".format(A,B,C))
