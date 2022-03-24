# goal_num = 0
# n = 0
# goal_len = 0
#
# record = []
# length = []
#
# def dfs(cnt, len, curnum):
#     if curnum == goal_num:
#         return 1
#
#     for i in range(cnt, n):
#         if record[i] or (i > 0 and record[i - 1] == 0 and length[i] == length[i - 1]):
#             continue
#
#         if len + length[i] == goal_len:
#             record[i] = 1
#             if dfs(0, 0, curnum + 1):
#                 return 1
#             record[i] = 0
#             return 0
#
#         elif len + length[i] < goal_len:
#             record[i] = 1
#             if dfs(i + 1, len + length[i], curnum):
#                 return 1
#             record[i] = 0
#             if len == 0:
#                 return 0
#
#     return 0
#
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     length = [int(x) for x in input().split()]
#     length.sort(reverse=True)
#
#     total = sum(length)
#     maxl = length[0]
#
#     for i in range(maxl, total + 1):
#         record = [0] * n
#         goal_len = i
#         if total % i == 0:
#             goal_num = int(total / i)
#             if dfs(0, 0, 0):
#                 print(i)
#                 break

def cut(lgt, lef, lst, num):
    if (num > 0 and lst == []) or (num == 1 and lef < lst[0]):
        return False
    while num > 0:
        lst.sort()
        twig = lst.pop()
        if lef > twig:
            return cut(lgt, lef-twig, lst, num)
        elif lef == twig:
            return cut(lgt, lgt, lst, num-1)
        else:
            cache = []
            cache.append(twig)
            while lst[-1] > lef:
                cache.append(lst.pop())
            n_twig = lst.pop()
            if n_twig == lef:
                lst.extend(cache)
                return cut(lgt, lgt, lst, num-1)
            else:
                lst.extend(cache)
                return cut(lgt, lef-n_twig, lst, num)
    return True


ans = []
while int(input()) != 0:
    sticks = list(map(int, input().split()))
    sticks.sort(reverse=True)
    sums = sum(sticks)
    prob = []
    for i in range(sticks[0], sums+1):
        if sums % i == 0:
            prob.append(i)
    sticks.sort()
    for j in range(len(prob)):
        if cut(prob[j], prob[j], sticks, int(sums/(prob[j]))):
            ans.append(prob[j])
            break
for p in ans:
    print(p)
