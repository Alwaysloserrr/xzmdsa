# T, M = [int(x) for x in input().split()]
#
# t, v = [], []
# for i in range(M):
#     a = [int(x) for x in input().split()]
#     t.append(a[0])
#     v.append(a[1])
#
# value = [0] * (T + 1)
# for i in range(M):
#     for j in range(T, 0, -1):
#         if t[i] > j:
#             continue
#         value[j] = max(value[j], value[j - t[i]] + v[i])
#
# print(value[T])
# print(value)
#
t, m = map(int, input().split())
alst = [(0, 0)]
for i in range(m):
    alst.append(tuple(map(int, input().split())))
ansdict = dict()


def herbSeeker(i, time):
    if (i, time) in ansdict.keys():
        return ansdict[(i, time)]
    else:
        if alst[i][0] == 0 or time == 0:
            ansdict[(i, time)] = 0
            return 0

        elif alst[i][0] > time:
            ansdict[(i, time)] = herbSeeker(i - 1, time)
            return herbSeeker(i - 1, time)

        else:
            f = max(herbSeeker(i - 1, time - alst[i][0]) + alst[i][1], herbSeeker(i - 1, time))
            ansdict[(i, time)] = f
            return f


print(herbSeeker(m, t))