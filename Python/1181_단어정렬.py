import sys
N = int(sys.stdin.readline())
A = [sys.stdin.readline().strip() for i in range(N)]
X = list(set(A))
X.sort(key= lambda x: (len(x), x) )
for j in X:
    print(j)