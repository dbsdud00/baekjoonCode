import sys
X = int(sys.stdin.readline())
for i in range(1,X+1):
    if (X <= i):
        if (i%2!=0):
            a = i - X +1
            b = X
        else:
            a = X
            b = i - X+ 1
        print(a,"/",b,sep="")
        break
    X = X-i