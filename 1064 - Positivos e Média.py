cont=0
soma=0
for i in range(6):
   nun=float(input())
   if nun>0:
     soma = soma+nun
     cont+=1
print('{} valores positivos'.format(cont))
print('{:.1f}'.format(soma/cont))