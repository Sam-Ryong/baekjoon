# 여러 줄에 걸친 입출력!

import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break