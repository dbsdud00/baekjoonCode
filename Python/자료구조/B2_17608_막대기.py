# 막대기를 세워두고 오른쪽에서 보았을 때 몇개가 보이는 지
import sys

N = int(sys.stdin.readline()) # 막대기 갯수
h = list(int(sys.stdin.readline()) for i in range(N))   # 막대기 높이 차례로
h = h[::-1]     # 막대기 역순 정렬
op = 1          
look = h[0]     
for i in range(1,len(h)):
    if look < h[i]:
        look = h[i]
        op += 1

print(op)