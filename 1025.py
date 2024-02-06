N, M = map(int, input().split())

matrix = []

result = -1

def checksquare(a):
    temp = 0
    global result
    num = int(a) 
    print(num)
    while (temp*temp < num):
        if (temp * temp == num):
            if (num > result):
                result = num
        temp = temp + 1

def seq(d,max):
    a = 0
    result = []
    while (max >= a):
        result.append(a)
        a = a + d
    
    return result


for i in range(N):
    num = input()
    matrix.append([])
    for j in range(M):
        matrix[i].append(int(num[j]))

for i in range(N):
    for j in range(M):
        if (i != 0 and j != 0):
            num = 0
            
            rowseq = seq(i,N-1)
            colseq = seq(j,M-1)


            for k in range(min(len(rowseq),len(colseq))):    
                num = str(num)
                num = num + str(matrix[rowseq[k]][colseq[k]])
            checksquare(num)
             

print(result)