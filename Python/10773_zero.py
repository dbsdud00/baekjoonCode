import sys
K = int(sys.stdin.readline())
don = []
for _ in range(K):
    n = int(sys.stdin.readline())
    if(n==0):
        don.pop()
    else:
        don.append(n)
print(sum(don))

