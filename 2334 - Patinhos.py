nun = 0
while (nun != -1):
    nun = int(input())
    if nun == 0:
        print(nun)
    elif nun >= 1 and nun <= 10 ** 19:
        print(nun - 1)
