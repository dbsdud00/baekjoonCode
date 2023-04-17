import sys
N = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(N)]
stack = []
for i in data:
    Q = i.split(' ')
    if Q[0]=='push':
        stack.insert(0,int(Q[1]))
    elif Q[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop(0))
    elif Q[0]=='size':
        print(len(stack))
    elif Q[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[0])
    

