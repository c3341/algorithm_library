#最小全域木をO(ElogV)で求める
#edge:(cost,u,v)の形
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
uf = UnionFind(n)
edge.sort()
ans = 0  #最小全域木のコスト
edge_cnt = 0
index = 0
while edge_cnt < n-1:
    cost,i,j = edge[index]
    if not uf.same(i,j):
        ans += cost
        uf.unite(i,j)
        edge_cnt += 1
    index += 1
