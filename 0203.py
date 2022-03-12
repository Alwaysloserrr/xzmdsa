n, m = [int(x) for x in input().split()]

record = [1] * n
cur_num = 1
cur_monkey = 0
ans = []
while sum(record) > 1:
    if cur_num == m:
        record[cur_monkey] = 0
        cur_num = 1
        ans.append(cur_monkey)
    else:
        cur_num += 1
    cur_monkey = (cur_monkey + 1) % n
    while record[cur_monkey] == 0:
        cur_monkey = (cur_monkey + 1) % n

print(' '.join([str(i + 1) for i in ans]))
for i in range(n):
    if record[i]:
        print(i + 1)
