import itertools
import math

n = int(input().strip())

perms = list(itertools.permutations(range(1, n + 1)))

print(math.factorial(n))
for p in perms:
    print(" ".join(map(str, p)))
