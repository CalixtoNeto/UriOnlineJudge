while True:
    try:
        while True:
            l = input().split()
            a = int(l[0])
            b = int(l[1])
            c = int(l[2])
            if a == 0 and b == 0 and c == 0:
                print("*")
                a = b = c = 0
            elif a == 1 and b == 1 and c == 0:
                print("C")
                a = b = c = 0
            elif a == 1 and b == 0 and c == 0:
                print("A")
                a = b = c = 0
            elif a == 1 and b == 0 and c == 1:
                print("B")
                a = b = c = 0
            elif a == 1 and b == 1 and c == 1:
                print("*")
                a = b = c = 0
            elif a == 0 and b == 0 and c == 1:
                print("C")
                a = b = c = 0
            elif a == 0 and b == 1 and c == 0:
                print("B")
                a = b = c = 0
            elif a == 0 and b == 1 and c == 1:
                print("A")
                a = b = c = 0
            elif a == 1 and b == 0 and c == 1:
                print("B")
                a = b = c = 0


    except:
        break