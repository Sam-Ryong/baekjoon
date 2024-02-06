T = int(input())

result = []

def travel(dis, remain, hop, casenum):
    global result

    remain = remain - dis

    if (dis <= 0 or remain < 0):
        return
    hop = hop + 1

    if (remain == 0 and dis == 1):
        if (result[casenum] == 0 or (result[casenum] > hop)):
            result[casenum] = hop
        return
    
    travel(dis-1,remain,hop,casenum)
    travel(dis,remain,hop,casenum)
    travel(dis+1,remain,hop,casenum)



for i in range(T):
    x, y = map(int, input().split())
    result.append(0)
    travel(1,y-x,0,i)

for i in range(T):
    print(result[i])


