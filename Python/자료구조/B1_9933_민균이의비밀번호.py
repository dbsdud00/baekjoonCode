import sys

N = int(sys.stdin.readline())
T = [sys.stdin.readline().strip() for i in range(N)]
for j in range(N):
    if T[j] == T[j][::-1]:
        print(len(T[j]),T[j][len(T[j])//2])
        break
    elif T[j][::-1] in T:
        print(len(T[j]),T[j][len(T[j])//2])
        break
    
