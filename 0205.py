n = int(input())

d = []

for _ in range(n):
    d.append([int(x) for x in input().split()])


for i in range(n):
    for j in range(n):
        if d[i][j] == 0:
            h = 0
            w = 0
            while i + h < n and d[i + h][j] == 0:
                h += 1
            while j + w < n and d[i][j + w] == 0:
                w += 1
            print((h - 2) * (w - 2))
            exit(0)

print(0)