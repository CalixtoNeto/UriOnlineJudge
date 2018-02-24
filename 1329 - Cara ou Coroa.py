n = int(input())

while n > 0:
    l = input().split(" ")
    cont1 = 0
    cont0 = 0

    for i in range(n):
        if l[i] == '0':
            cont0 += 1
        elif l[i] == '1':
            cont1 += 1
    print('Mary won {} times and John won {} times'.format(cont0, cont1))
    n = int(input())