# cases = int(input())
# for _ in range(cases):
#     l1 = [int(x) for x in input().split()][:-2]
#     l2 = [int(x) for x in input().split()][:-2]
#
#     dic = {}
#     len1 = int(len(l1) / 2)
#     len2 = int(len(l2) / 2)
#
#     for i in range(len1):
#         if l1[i * 2 + 1] in dic.keys():
#             dic[l1[i * 2 + 1]] += l1[i * 2]
#         else:
#             dic[l1[i * 2 + 1]] = l1[i * 2]
#
#     for i in range(len2):
#         if l2[i * 2 + 1] in dic.keys():
#             dic[l2[i * 2 + 1]] += l2[i * 2]
#         else:
#             dic[l2[i * 2 + 1]] = l2[i * 2]
#
#     ans = []
#     keys = list(dic.keys())
#     keys.sort(reverse=True)
#
#     for key in keys:
#         if dic[key] == 0:
#             continue
#         ans.append("[ {} {} ]".format(dic[key], key))
#
#     print(' '.join(ans))

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        if self.items!=[]:
            return self.items[-1]
        else:
            return -1
    def Sort(self):
        return self.items.sort()
def Plus(k1,k2):
    s1 = Stack()
    s2 = Stack()
    for i in k1:
        s1.push(i)
    for i in k2:
        s2.push(i)
    s1.Sort()
    s2.Sort()
    while max(s1.size(),s2.size())>0:
        if s1.peek()>s2.peek():
            a = s1.pop()
            if a >0 and s1.size()>0:
                print("[ {} {} ] ".format(k1[a],a),end="")
            else:
                print("[ {} {} ]".format(k1[a],a))
        elif s1.peek()<s2.peek():
            a = s2.pop()
            if a >0 and s2.size()>0:
                print("[ {} {} ] ".format(k2[a],a),end="")
            else:
                print("[ {} {} ]".format(k2[a],a))
        elif s1.peek()==s2.peek():
            a = s1.pop()
            b = s2.pop()
            if a >0 and max(s1.size(),s2.size())>0:
                if k1[a]+k2[a]!=0:
                    print("[ {} {} ] ".format(k1[a]+k2[a],a),end="")
            else:
                print("[ {} {} ]".format(k1[a]+k2[a],a))
n = int(input())
lst = [[] for i in range(2*n)]
for i in range(2*n):
    lst[i] = list(input().split())
    lst[i].pop()
    lst[i].pop()
for i in range(0,2*n-1,2):
    k1 =dict()
    k2 = dict()
    for j in range(0,len(lst[i])-1,2):
        k1[int(lst[i][j+1])] = int(lst[i][j])
    for j in range(0,len(lst[i+1])-1,2):
        k2[int(lst[i+1][j+1])] = int(lst[i+1][j])
    Plus(k1,k2)