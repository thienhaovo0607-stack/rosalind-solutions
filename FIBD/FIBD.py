n, m = map(int, input().split())

rabbits = [0] * m
rabbits[0] = 1

for month in range(2, n + 1):
    newborns = sum(rabbits[1:])
    rabbits = [newborns] + rabbits[:-1]

print(sum(rabbits))
