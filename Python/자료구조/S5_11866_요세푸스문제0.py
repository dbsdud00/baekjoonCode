# 구현 , 자료구조, 큐
import sys

N,K = map(int,sys.stdin.readline().split())

people = list(int(i+1) for i in range(N))
out = 0
index = 0
print('<',end="")
while N:
    if index + K <=N:
        index = index+K-1
        out = people.pop(index)
        N-=1
        if N != 0:
            print(out, end=", ")
    else:
        while(index+K>N):
            index = index-N
            
print(out,'>',sep="")



# 1234567
# 12345671 append
# 2345671 push
# 23456712 append
# 3456712 push





# people = [int(i+1) for i in range(N)]
# print(people)
# loof,out = 0,0
# # print('<',end="")
# while people:
#     if out+K <= N:
#         out = people.pop(out+K-1)
#         N-=1
#         print(out)
#     else:
#         while(out+K<=N):
#             out -= N
#         out = people.pop(K+out-N)
#         N-=1
#         print(out)
#         if N == 0 : break

        