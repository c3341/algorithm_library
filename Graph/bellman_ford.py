#単一頂点最短距離、グラフに負の重みがあったり不閉路を検出するとき使う(O(V*E))
def bellman_ford(V,G,start=0):
    dist = [inf]*V
    dist[start]=0
    negative_cycle = False
    for _ in range(1,V):
        for u in G:
            for v,d in G[u]:
                if dist[v]>dist[u]+d:
                    dist[v] = dist[u]+d
    for u in G:
        for v,d in G[u]:
            if dist[v] > dist[u]+d:
                negative_cycle = True
    if negative_cycle:
        return -1
    else:
        return dist
