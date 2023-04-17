# 할리갈리 게임 상황에 따라 종을 쳐야하는지 출력

import sys

N = int(sys.stdin.readline())

H = {'STRAWBERRY':0, 'BANANA':0, 'LIME':0, 'PLUM':0}

for _ in range(N):
    a, b = sys.stdin.readline().split()
    H[a] += int(b)

print('YES' if 5 in H.values() else 'NO')



# N = int(sys.stdin.readline())
# X = [list(map(str,sys.stdin.readline().split())) for i in range(N)]

# STRAWBERRY = 0
# BANANA = 0
# LIME = 0
# PLUM = 0

# for i in range(N):
#     if X[i][0] == 'STRAWBERRY':
#         STRAWBERRY += int(X[i][1])
#     elif X[i][0] == 'BANANA':
#         BANANA += int(X[i][1]) 
#     elif X[i][0] == 'LIME':
#         LIME += int(X[i][1])
#     else:
#         PLUM += int(X[i][1])    
        
# if STRAWBERRY == 5 or BANANA == 5 or LIME == 5 or PLUM == 5:
#     print("YES")
# else: print("NO")

