# 나무 M미터 필요해서 나무 벌목
# N 개의 나무가 존재
# 목재 절단기 높이 H미터 지정
# input: N(나무의 수) M(필요한 나무 길이)
# input: 나무의 높이*N

import sys

N,M = map(int,sys.stdin.readline().split())
X = [int(x) for x in sys.stdin.readline().split()]

start, end = 1,max(X)

while(start<=end):
    mid = (start+end)//2
    
    log = 0
    for i in X:
        if mid<i:
            log+=i-mid
    # print("start : ", start,"/ mid : ",mid, "/ end : ", end, "/ log : ", log)
    if log >= M:
        start = mid +1
    else :
        end = mid - 1
        
print(end)








# X.sort(reverse=True)
# namu = X[0]-X[1]
# for i in range(len(X)-1):
#     if namu > M:
#         namu = X[i+1] + (namu-M)//(i+1)
#         print(1,i,X[i+1],(namu-M)//(i+1),namu)
#         break
#     elif namu == M:
#         namu = X[i+1]
#         print(2,i,namu)
#         break
#     else:
#         namu = namu + (X[i+1]-X[i+2])*(i+2)
#         print(3,i,namu,(X[i+1]-X[i+2])*(i+2))
# print(namu)




