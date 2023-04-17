


import sys

N = int(sys.stdin.readline())   # 학생 수
T = list(map(int,sys.stdin.readline().split())) # 학생들이 고른 숫자 차례로

op = []

for i in range(N):
    op.insert(i-T[i],i+1)

for j in op:
    print(j,end=" ")
