n = int(input())

nums = [int(x) for x in input().split()]
dp = [nums[0]]
# dp[i]表示长度为i + 1的下降序列的最小的数的最大值
for i in range(n - 1):
    cur = nums[i + 1]
    if cur <= dp[-1]:
        dp.append(cur)
    elif cur > dp[0]:
        dp[0] = cur
    else:
        for j in range(len(dp) - 1, 0, -1):
            if cur < dp[j - 1]:
                dp[j] = cur
                break

print(len(dp))