import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
A.sort()
M = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))

for i in X:
    if bisect_right(A,i) - bisect_left(A,i):
        print(1)
    else : print(0)


# a = int(sys.stdin.readline())
# l = set(int(x) for x in sys.stdin.readline().split())
# b = int(sys.stdin.readline())
# chk = [int(x) for x in sys.stdin.readline().split()]


# for i in X:
#     if i in A:
#         print(1)
#     else:
#         print(0)

