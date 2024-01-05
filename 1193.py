X = int(input())

result = [1,1]

num = 1
sum = 1

while sum < X:
    num = num + 1

    sum = sum + num

if (num % 2 == 0): #짝수이면
    mother = num - sum + X
    son = num - mother + 1
    result = [mother ,  son]

elif (num % 2 == 1):
    mother = num - sum + X
    son = num - mother + 1
    result = [son ,  mother]

print(result[0],"/",result[1],sep="")