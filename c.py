n, m = int(input()), int(input())
l = []
count = 1
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(count)
        count += 1
    l.append(temp)
#print(*l, sep = '\n')

def rota(lis):
    n, m = len(lis), len(lis[0])
    temp = [[0] * n for _ in range(m)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp[i - 1][j - 1] = lis[-j][-i]
    return temp

def rotb(lis):
    m, n = len(lis), len(lis[0])
    temp = [[0] * n for _ in range(m)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp[j - 1][i - 1] =  lis[-j][-i]
    return temp

d = rota(l)
print(*d, sep = '\n')
s = rotb(d)
print(s)