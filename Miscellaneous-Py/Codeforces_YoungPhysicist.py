T = int(input())
L2=[]
sx=0
sy=0
sz=0
for _ in range(T):
    L=input().split()
    sx+=int(L[0])
    sy+=int(L[1])
    sz+=int(L[2])
    
if sx==0 and sy==0 and sz==0:
    print("YES")
    
else:
    print("NO")
