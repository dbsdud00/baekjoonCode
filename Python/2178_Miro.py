import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().strip())) for i in range(N)]

# 상(-1,0), 하(1,0), 좌(-1,0), 우(1,0)
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()   # x,y에 현재 위치 저장
        for i in range(4):      # 현재위치에서 상하좌우 4방향으로 진행했을 때
            nx = x + dx[i]      # 진행한 위치를 nx, ny에 저장
            ny = y + dy[i]      # 4방향으로 진행했을 때 범위 내이고 그래프상 1인 곳만 통과
            if 0 <=nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx,ny))               # 진행하는 위치 저장 후 
                graph[nx][ny] = graph[x][y] +1      # 현재 위치에 1 더해서 이동 칸수 저장

    return graph[N-1][M-1]      # N*M 위치의 이동 칸수 리턴

print(bfs(0,0))