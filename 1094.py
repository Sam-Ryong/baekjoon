X = int(input())

stick = [64]

while sum(stick) > X:
    short = min(stick)//2
    stick.remove(min(stick))
    stick.append(short)
    if (sum(stick) < X):
        stick.append(short)

print(len(stick))

    