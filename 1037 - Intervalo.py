X = float(input())

if X >= 0 and X <= 25 :
    print("Intervalo [0,25]")
else:
    if 25 < X <= 50:
        print("Intervalo (25,50]")
    else:
        if 50 < X <= 75:
            print("Intervalo (50,75]")
        else:
            if 75 < X <= 100:
                print("Intervalo (75,100]")
            else:
                print("Fora de intervalo")


