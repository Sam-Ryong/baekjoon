N, K = map(int, input().split())


num = 2
bottles = []
holding = N
remain = []

while (sum(bottles) < N):
    exp = 0
    while (num**exp <= holding):
        exp = exp + 1
    bottles.append(num**(exp-1))
    holding = holding - num**(exp-1)

remain = bottles[K+1:]
bottles = bottles[0:K+1]


result = bottles[len(bottles)-2] - sum(remain) - bottles[-1]

print(result)
