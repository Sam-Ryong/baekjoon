N, r, c = map(int, input().split())

length = 2**N
maxnum = (2**N)**2
minnum = 0

while True:
    length = length // 2
    if length < 2:
        break
    if (r >= length):
        minnum = (maxnum + minnum) // 2
        r = r - length
    else:
        maxnum = (maxnum + minnum) // 2
    
    if (c >= length):
        minnum = (maxnum + minnum) // 2
        c = c - length
    else:
        maxnum = (maxnum + minnum) // 2

matrix = [[minnum, minnum + 1],[minnum + 2, minnum + 3]]

print(matrix[r%2][c%2])