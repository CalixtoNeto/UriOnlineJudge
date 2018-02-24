quantidade=int(input())
cont1=151
lista=[]
for i in range (quantidade):
  nome=input().upper()
  lista.append(nome)
  if lista.count(nome) == True:
    cont1 = cont1 - 1
print('Falta(m) {} pomekon(s).'.format(cont1))