T = int(input())
signal = []
result = "NO"

def node(statenum, sig, i):
    global result
    char = sig[i]

    if statenum == 0:
        if char == "0":
            node(5,sig,i+1)
        elif char == "1":
            node(1,sig,i+1)
    elif statenum == 1:
        if char == "0":
            node(2,sig,i+1)
        elif char == "1":
            return
    elif statenum == 2:
        if char == "0":
            node(3,sig,i+1)
        elif char == "1":
            return
    elif statenum == 3:
        if char == "0":
            node(3,sig,i+1)
        elif char == "1":
            node(4,sig,i+1)
    elif statenum == 4:
        if char == "0":
            node(5,sig,i+1)
        elif char == "1":
            node(4,sig,i+1)
            node(1,sig,i+1)
        elif char == "X":
            result = "YES"
            return
    elif statenum == 5:
        if char == "0":
            return
        elif char == "1":
            node(6,sig,i+1)
    elif statenum == 6:
        if char == "0":
            node(5,sig,i+1)
        elif char == "1":
            node(1,sig,i+1)
        elif char == "X":
            result = "YES"
            return


for i in range(T):
    test = input()
    test = test+"X"
    signal.append(test)

for i in range(T):
    node(0,signal[i],0)
    print(result)
    result = "NO"

