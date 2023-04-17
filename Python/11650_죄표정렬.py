import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[0], x[1]))
for i in so:
    print(i[0], i[1])





# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# xy = list(sys.stdin.readline().split() for i in range(N))

# sort_xy = deque([xy[0]])

# for n in range(1,N):
#     if sort_xy[n-1][0]<xy[n][0]:
#         sort_xy.append(xy[n])
#     else:
#         for j in range(n):
#             if sort_xy[j][0] > xy[n][0]:
#                 sort_xy.insert(j,xy[n])
#                 break
#             if sort_xy[j][0] == xy[n][0]:
#                 if sort_xy[j][1]>xy[n][1]:
#                     sort_xy.insert(j,xy[n])
#                     break
#                 else : 
#                     sort_xy.insert(j+1,xy[n])
#                     break
                
# for k in range(N):
#     print(int(sort_xy[k][0]),int(sort_xy[k][1]))
    
    
    
    
    
    
    # if(sort_xy[0][0]>xy[n][0]):
    #     sort_xy.appendleft(xy[n])
    #     if sort_xy[0][0]==xy[n][0]:
    #         if sort_xy[0][1]<xy[n][0]:
    #             sort_xy.insert(1,xy[n])
    #         else : sort_xy.appendleft(xy[n])
    # elif sort_xy[n-1][0]<xy[n][0]:
    #     sort_xy.append(xy[n])
    #     if sort_xy[n-1][0]==xy[n][0]:
    #         if sort_xy[n-1][1]>xy[n][1]:
    #             sort_xy.insert(n-2,xy[n])
    #         else : sort_xy.append(xy[n])
    # elif sort_xy[0][0]<xy[n][0]:
    #     for j in range(len(sort_xy)-1):
    #         if sort_xy[j+1][0] > xy[n][0]:
    #             sort_xy.insert(j+1,xy[n])
    #         if sort_xy[j+1][0] == xy[n][0]:
    #             if sort_xy[n-1][1]>xy[n][1]:
    #                 sort_xy.insert(n-2,xy[n])
    #             else : sort_xy.append(xy[n])
                
    # else
