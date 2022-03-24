dp = [[0] * 51 for _ in range(51)]
# dp[i][j] i这个数，拆成最大值不大于j的组合数
for i in range(1, 51):
    dp[1][i] = 1
    dp[i][1] = 1
    dp[0][i] = 1

for i in range(2, 51):
    for j in range(2, 51):
        if i >= j:
            dp[i][j] = dp[i][j - 1] + dp[i - j][j]
        else:
            dp[i][j] = dp[i][i]

while True:
    try:
        n = int(input())
        print(dp[n][n])
    except EOFError:
        break
