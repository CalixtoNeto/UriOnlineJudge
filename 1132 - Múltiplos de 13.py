n1=int(input())
n2=int(input())

if (n2<n1):
  aux = n1
  n1  = n2
  n2  = aux
cont=0
for i in range (n1,n2+1):
  if i%13 !=0:
    cont +=i
print(cont)