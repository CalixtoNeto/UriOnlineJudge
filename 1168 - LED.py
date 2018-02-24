n = int(input())
for z in range(n):
    s=input()
    result=0
    for i in s:
        if i == "1":
            result+=2
        if i == "2":
            result+=5
        if i == "3":
            result+=5
        if i == "4":
            result+=4
        if i == "5":
            result+=5
        if i == "6":
            result+=6
        if i == "7":
            result+=3
        if i == "8":
            result+=7
        if i == "9":
            result+=6
        if i == "0":
            result+=6
    print("{} leds".format(result))