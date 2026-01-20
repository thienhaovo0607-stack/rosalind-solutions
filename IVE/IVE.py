a, b, c, d, e, f = map(int, input().split())

expected = 2 * (
    a * 1 +
    b * 1 +
    c * 1 +
    d * 0.75 +
    e * 0.5 +
    f * 0
)

print(expected)