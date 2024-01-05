n = int(input())
result = []
templist = []

for i in range(n):
    word = input()
    result.append(word)

result = list(set(result))
result = sorted(result)

print("----------------------------")
# 삽입 정렬

while True:
    for i in range(len(result)//2):
        if (len(result[i]) > len(result[i+1])):
            templist.append(result[i+1])
            templist.append(result[i])
    


for i in range(len(result)):
    print(result[i])
