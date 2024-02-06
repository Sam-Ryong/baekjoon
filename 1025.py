N, M = map(int, input().split())

matrix = []

result = -1

def checksquare(num):
    temp = 0
    global result
    while (temp*temp <= num):
        if (temp * temp == num):
            if (num > result):
                result = num
        temp = temp + 1

def travel(i,j,di,dj,reg):
    global matrix

    if ((i > N - 1) or (j > M - 1)):
        return
    if ((i < 0) or (j < 0)):
        return
    reg = reg + str(matrix[i][j])
    checksquare(int(reg))
    if (di == 0 and dj == 0):
        return
    travel(i+di,j+dj,di,dj,reg)


for i in range(N):
    num = input()
    matrix.append([])
    for j in range(M):
        matrix[i].append(int(num[j]))

for i in range(N):
    for j in range(M):
        for k in range(N):
            for m in range(M):
                travel(i,j,k,m,"")
                travel(i,j,k,(-1 * m),"")
                travel(i,j,(-1 * k),m,"")
                travel(i,j,(-1 * k),(-1 * m),"")

print(result)