from itertools import product

e = enumerate

for p in [1, 2]:
    g = {
        (x, y) + (0,) * p for x, r in e(open("input.txt")) for y, c in e(r) if c == "#"
    }
    print(g)

    def a(c):
        n = len(g & set(product(*[range(a - 1, a + 2) for a in c])))
        return n == 4 and c in g or n == 3

    for r in range(6):
        g = set(filter(a, product(range(-r - 1, r + 8), repeat=2 + p)))

    print(len(g))
