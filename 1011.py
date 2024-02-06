T = int(input())

result = []
distance = []

def travel(dis):
    hop = 2
    if (dis == 0):
        result.append(0)
        return
    if (dis == 1):
        result.append(1)
        return
    else:
        while True:
            if (hop%2 == 0):
                num = int((((1 + hop//2) / 2) * hop//2) * 2)
            
            elif (hop%2 == 1):
                num = int((((1 + (hop-1)//2) / 2) * (hop-1)//2) * 2 + (hop-1)//2 + 1)
            
            if (num >= dis):
                break
            
            hop = hop + 1
    
    result.append(hop)

for i in range(T):
    x, y = map(int, input().split())
    distance.append(y-x)

for i in range(T):
    travel(distance[i])

for i in range(T):
    print(result[i])


