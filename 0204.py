cases = int(input())
for _ in range(cases):
    l1 = [int(x) for x in input().split()][:-2]
    l2 = [int(x) for x in input().split()][:-2]

    dic = {}
    len1 = int(len(l1) / 2)
    len2 = int(len(l2) / 2)

    for i in range(len1):
        if l1[i * 2 + 1] in dic.keys():
            dic[l1[i * 2 + 1]] += l1[i * 2]
        else:
            dic[l1[i * 2 + 1]] = l1[i * 2]

    for i in range(len2):
        if l2[i * 2 + 1] in dic.keys():
            dic[l2[i * 2 + 1]] += l2[i * 2]
        else:
            dic[l2[i * 2 + 1]] = l2[i * 2]

    ans = []
    keys = list(dic.keys())
    keys.sort(reverse=True)

    for key in keys:
        if dic[key] == 0:
            continue
        ans.append("[ {} {} ]".format(dic[key], key))

    print(' '.join(ans))
