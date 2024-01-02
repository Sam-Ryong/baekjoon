product = []
temp = []

result = 0

N, K = map(int, input().split())

for i in range(N):
    w, v = map(int, input().split())
    product.append([w,v])
    temp.append([])
    for j in range(K):
        temp[i].append(0)
