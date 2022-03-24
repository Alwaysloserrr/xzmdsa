# n = int(input())
#
# d = []
#
# for _ in range(n):
#     d.append([int(x) for x in input().split(" ")])
#
#
# for i in range(n):
#     for j in range(n):
#         if d[i][j] == 0:
#             h = 0
#             w = 0
#             while i + h < n and d[i + h][j] == 0:
#                 h += 1
#             while j + w < n and d[i][j + w] == 0:
#                 w += 1
#             print((h - 2) * (w - 2))
#             exit(0)
#
# print(0)
n = input()
n = int(n)
M = [[0 for i in range(0, n)] for i in range(0, n)]
Pass = [[0 for i in range(0, n)] for i in range(0, n)]
for i in range(0, n):
    M[i] = input().split()
    for j in range(0, n):
        M[i][j] = int(M[i][j])


def walkable(x, y):
    if M[y][x] == 0:
        return True;

    Pass[y][x] = 1

    if y < n - 1 and Pass[y + 1][x] == 0 and M[y + 1][x] == 255:
        return walkable(x, y + 1)
    elif y == n - 1:
        return True

    if x < n - 1 and Pass[y][x + 1] == 0 and M[y][x + 1] == 255:
        return walkable(x + 1, y)
    elif x == n - 1:
        return True

    if y > 0 and Pass[y - 1][x] == 0 and M[y - 1][x] == 255:
        return walkable(x, y - 1)
    elif y == 0:
        return True

    if x > 0 and Pass[y][x - 1] == 0 and M[y][x - 1] == 255:
        return walkable(x - 1, y)
    elif x == 0:
        return True

    return False


cnt = 0
for i in range(0, n):
    for j in range(0, n):
        Pass = [[0 for i in range(0, n)] for i in range(0, n)]
        if not walkable(i, j):
            cnt += 1

print(cnt)
