T = int(input())

location = []
distance = []
result = []

for i in range(T):
    x, y = map(int, input().split())
    location.append([x,y])
    distance.append(x-y)

for i in range(T):
    start = location[i][0]
    end = location[i][1]
    distance = distance[i]


        


