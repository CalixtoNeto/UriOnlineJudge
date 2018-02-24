dias = int(input())
ano = 0
mes = 0
dia = 0
while (dias >= 365):
  dias=dias-365
  ano+=1
while (dias >= 30):
  dias=dias-30
  mes+=1
while (dias >= 1):
  dias=dias-1
  dia+=1
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))