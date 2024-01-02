def fact(n):
    factorial = 1
    while (n > 1):
        factorial = factorial * n
        n = n - 1
    return factorial

n = int(input())
result = []

for i in range(n):
    N, M = map(int, input().split())
    comb = (fact(M)//fact(N))//fact(M-N)
    if (N == 0):
        comb = 0
    result.append(comb)

for i in range(n):
    print(result[i])
