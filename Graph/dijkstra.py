#dijkstra法,ALDS1_12_Cでverify
V = int(input())
G = defaultdict(list)
for i in range(V):
    u,k,*vc = map(int,input().split())
    G[u] = [(v,c) for v,c in zip(vc[::2],vc[1::2])]
#dijkstra法、単一頂点からの最短経路を計算二分ヒープでO((E+V)logV)
def dijkstra(v):
    dist = [inf]*V
    dist[v] = 0
    hq = [(0,v)]

    while hq:
        p = heappop(hq)[1]
        for (q,c) in G[p]:
            if dist[q]>dist[p]+c:
                dist[q] = dist[p]+c
                heappush(hq,(dist[p]+c,q))
    return dist

d = dijkstra(0)
for i in range(V):
    print(i,d[i])
