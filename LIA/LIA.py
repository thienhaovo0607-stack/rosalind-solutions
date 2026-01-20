import math

k, N = map(int, input().split())

n = 2 ** k
p = 0.25

prob = 0
for i in range(N):
    prob += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))

print(1 - prob)
