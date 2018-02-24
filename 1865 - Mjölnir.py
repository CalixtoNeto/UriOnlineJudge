n=int(input())
for i in range(n):
    nome, newt=input().split()
    nome, newt=str(nome), int(newt)
    if nome == "Thor":
        print("Y")
    else:
        print("N")