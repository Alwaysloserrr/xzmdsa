n = int(input())

if n == 1:
    print(1)
    exit(0)

size = 2 * n - 1
num = size ** 2

ans = [[0] * (size) for i in range(size)]
ans[0][n - 1] = 1

row = 0
col = n - 1

cnt = 1

while cnt <= num:
    ans[row][col] = cnt
    cnt += 1
    new_row = (row + size - 1) % size
    new_col = (col + 1) % size
    if ans[new_row][new_col] > 0:
        row = (row + 1) % size
    else:
        row = new_row
        col = new_col

for i in range(size):
    print(' '.join([str(ans[i][j]) for j in range(size)]))
