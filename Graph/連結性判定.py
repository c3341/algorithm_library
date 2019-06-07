#グラフが連結であることを判定するO((E+V)logV)
#UnionFindで実装

V,E = map(int,input().split())
connectivity = True
class UnionFind():
    def __init__(self, N):
        self.rank = [0] * N
        self.par = [i for i in range(N)]
        self.counter = [1] * N

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            z = self.counter[x] + self.counter[y]
            self.counter[x], self.counter[y] = z, z
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def size(self, x):
        x = self.find(x)
        return self.counter[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

for i in range(E):
    a,b = map(int,input().split()) #a,bを結ぶ辺の情報を受け取る
    uf.unite(a,b)
for i in range(N):
    if not uf.same(0,i):
        connectivity = False
        break
    
