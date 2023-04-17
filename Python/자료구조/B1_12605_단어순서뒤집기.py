import sys

N = int(sys.stdin.readline())

for i in range(N):
    t = list(map(str,sys.stdin.readline().split()))
    print(f"Case #{i+1}: ",end="")
    print(" ".join(j for j in t[::-1]))

