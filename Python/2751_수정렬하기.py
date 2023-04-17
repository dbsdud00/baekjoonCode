import sys
N = int(sys.stdin.readline())
X = [int(sys.stdin.readline().strip()) for i in range(N)]

X.sort()
for j in X:
    print(j)