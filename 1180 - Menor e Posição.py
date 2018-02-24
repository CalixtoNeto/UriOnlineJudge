input()
arr = [int(x) for x in input().split()]
n = min(arr)

print("Menor valor: {}".format ( n, sep=''))
print("Posicao: {}".format(arr.index(min(arr)), sep=''))