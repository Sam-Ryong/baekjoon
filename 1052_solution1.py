N, K = map(int, input().split())

temp = N
count = 0
while str(bin(temp)).count('1') > K:
    temp = temp + 1
    count = count + 1

print(count)