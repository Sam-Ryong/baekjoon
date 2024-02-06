N, M = map(int, input().split())

A = []
B = []
result = []

def func(row,col,A,B,n):
    global N,M,result 
    tempA = []
    tempB = []
    for i in range(N):
        tempA.append([])
        tempB.append([])
        for j in range(M):
            tempA[i].append(A[i][j])
            tempB[i].append(B[i][j])
    
    if (M - col < 3):
        row = row + 1
        col = 0
    
    if (N - row < 3):
        return
    
    for i in range(3):
        for j in range(3):
            tempA[i+row][j+col] = tempB[i+row][j+col]
    n = n + 1
    
    if (tempA == tempB):
        result.append(n)
        return
    else:
        func(row, col+1, tempA, tempB, n)
        func(row, col+1, A, B, n-1)

for i in range(N):
    row = input()
    A.append([])
    for i in range(M):
        A[-1].append(int(row[i]))

for i in range(N):
    row = input()
    B.append([])
    for i in range(M):
        B[-1].append(int(row[i]))

print(A==B)

func(0,0,A,B,0)

if (len(result) == 0):
    print(-1)
else:
    print(min(result))
print(result)
