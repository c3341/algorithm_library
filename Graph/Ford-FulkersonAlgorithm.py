#フォードファルカーソン(O(FE))
class FordFulkerson:
    def __init__(self,N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self,fr,to,cap):
        forward = [to,cap,None]
        forward[2] = backward = [fr,0,forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
        
　　#増加パスをDFSで増やす
    def dfs(self,v,t,f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            w,cap,rev = e
            if cap and not used[w]:
                d = self.dfs(w,t,min(f,cap))
                if d:
                    e[1] -=d
                    rev[1] += d
                    return d
        return 0

    def flow(self,s,t):
        flow = 0
        f = inf
        N = self.N
        while f:
            self.used = [0]*N
            f = self.dfs(s,t,inf)
            flow += f
        return flow

V,E = map(int,input().split())
ff = FordFulkerson(V)
for i in range(E):
    v0,v1,c = map(int,input().split())
    ff.add_edge(v0,v1,c)

print(ff.flow(0,V-1))
