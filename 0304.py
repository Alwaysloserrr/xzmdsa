r, c = [int(x) for x in input().split()]

Map = [[int(x) for x in input().split()] + [-1] for _ in range(r)]

value = [[0] * c for _ in range(r)]


def dfs(x, y):
    global r, c, Map, value

    if value[x][y]:
        return value[x][y]

    res = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > -1 and ny > -1 and nx < r and ny < c and Map[nx][ny] > Map[x][y]:
            res = max(res, dfs(nx, ny) + 1)

    value[x][y] = res
    return res



ans = 1
for i in range(r):
    for j in range(c):
        ans = max(ans, dfs(i, j))

print(ans)
