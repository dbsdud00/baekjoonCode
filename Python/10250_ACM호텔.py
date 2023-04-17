T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())
    a = N//H+1
    b = N%H
    if N % H == 0:  # h의 배수이면,
        a = N//H
        b = H
    op = 100*b+a
    print(op)


