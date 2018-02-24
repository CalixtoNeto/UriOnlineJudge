notas = float(input())
valor = notas
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0
m050 = 0
m25 = 0
m10 = 0
m5 = 0
m01 = 0


#contando notas
while (notas >= 100.00):
    notas = notas -100.00
    nota100 += 1
while (notas >= 50.00):
    notas = notas - 50.00
    nota50 += 1
while (notas >= 20.00):
    notas = notas - 20.00
    nota20 += 1
while (notas >= 10.00):
    notas = notas - 10.00
    nota10 += 1
while (notas >= 5.00):
    notas = notas - 5.00
    nota5 += 1
while (notas >= 2.00):
    notas = notas - 2.00
    nota2 += 1
#contando moedas
while (notas >= 1):
    notas = notas - 1
    nota1 += 1
while notas > 0.50 :
    notas = notas - 0.50
    m050 += 1
while notas >= 0.25 :
    notas = notas - 0.25
    m25 += 1
while notas >= 0.10 :
    notas = notas - 0.10
    m10 += 1
while notas >= 0.05 :
    notas = notas - 0.05
    m5 += 1
while notas >= 0.01 :
    notas = notas - 0.01
    m01 += 1


print("NOTAS:\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00".format(nota100,nota50,nota20,nota10,nota5,nota2))
print("MOEDAS:\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01".format(nota1,m050,m25,m10,m5,m01))

