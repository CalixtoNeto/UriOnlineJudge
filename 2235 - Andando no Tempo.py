linha=input().split(" ")
a=int(linha[0])
b=int(linha[1])
c=int(linha[2])


if c == a or (a+c)==b or (a+b)==c or (b+c)==a or a==b or b==c:
  print("S")

else:
  print("N")