import sys

N = int(sys.stdin.readline())
N_card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_card = list(map(int,sys.stdin.readline().split()))






print(N_card)
print(M_card)



# N = int(sys.stdin.readline())
# N_card = sorted(list(map(int,sys.stdin.readline().split())))
# M = int(sys.stdin.readline())
# M_card = list(map(int,sys.stdin.readline().split()))
# same = [0]*(N)
# start, end = 0, N-1
# m,n=0
# while(N_card):
#     mid = (start+end)//2
#     if M_card[m] == N_card[mid]:
#         same[m]+=1
#         N_card.remove(mid)
#     elif M_card[m] < N_card[mid]:
#         end = mid
#     elif M_card[m] > N_card[mid]:
#         start = mid






# print(N_card)
# print(M_card)
    