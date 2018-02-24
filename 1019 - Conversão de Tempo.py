n = int(input())
horas=0
minutos=0
segundos=0
while n >= 3600:
    n = n-3600
    horas+=1
while n >= 60:
    n = n - 60
    minutos += 1
segundos = n
print("{}:{}:{}".format(horas,minutos,segundos))


