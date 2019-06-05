#N以下の素数を全て列挙O(NloglogN)
#N = int(input())
p = [1]*(N+1)
p[0]=p[1]=0
for x in range(2,int(sqrt(N)+1)):
    if p[x]:
        for y in range(x*x,N+1,x):
            p[y] = 0
