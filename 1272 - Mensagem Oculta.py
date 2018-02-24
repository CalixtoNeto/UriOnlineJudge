n = int(input())
for i in range(n):
    msg = input()
    msg = msg.split()
    a = len(msg)
    b = 0
    d = []
    e = ''
    while a < 50 and a > 0:
        a -= 1
        c = (msg[b][0])
        b += 1
        d.append(c)
    print(e.join(d))

