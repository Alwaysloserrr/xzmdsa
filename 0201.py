def get_record(x, ans):
    t = 1
    for i in range(16):
        ans[i] += 1 if t & x > 0 else 0
        t *= 2
    return ans


n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
record = [0] * 16
need_to_add = 0

for num in nums:
    record = get_record(num, ans=record)

for _ in range(m):
    action, n = input().split()

    if action == 'Q':
        if need_to_add != 0:
            nums = [(i + need_to_add) % 65536 for i in nums]
            need_to_add = 0
            record = [0] * 16
            for num in nums:
                record = get_record(num, ans=record)

        print(record[int(n)])
    else:
        need_to_add += int(n)
