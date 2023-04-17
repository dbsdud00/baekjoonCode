import sys
from collections import deque

N = int(sys.stdin.readline())
X = [list(map(str,sys.stdin.readline().strip())) for k in range(N)]
# input ex : (())()) -> NO

# False
for j in range(N):
    li =  []
    right = True
    for k in X[j]:
        if k == '(':
            li.append(k)
        elif k == ')':
            if li:
                li.pop()
            else :
                right=False
                break
    if not li and right :
        print("Yes")
    else : print("No")

# True
# for i in range(N):
#     stack = []
#     for j in X[i]:
#         if j == '(':
#             stack.append(j)
#         elif j == ')':
#             if stack:
#                 stack.pop()
#             else: # 스택에 괄호가 없을경우 NO
#                 print("NO")
#                 break
#     else: # break문으로 끊기지 않고 수행됬을경우 수행한다
#         if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
#             print("YES")
#         else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
#             print("NO")



# for j in range(N):
#     li = []
#     for k in range(len(X[j])):
#         if X[j][k] == '(':
#             li.append("1")
#         else :
#             if len(li) !=0:
#                 li.pop()
#             else :
#                 print(j,"NO")
#                 break
#     if len(li) !=0:
#         print(j,"Yes")
#     else : print(j,"NO")

