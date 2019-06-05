#V:頂点数
#G[i][j]:(i,j)間の距離

#全頂点対間の最短距離O(VE)
def warshallfloyd(V,G):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                G[i][j] = min(G[i][j],G[i][k]+G[k][j])

def main():
    V,E = map(int,input().split())
    G = [[inf]*V for _ in range(V)]
    for i in range(V):
        G[i][i]=0
    for _ in range(E):
        u,v,d = map(int,input().split())
        G[u-1][v-1] = d
        G[v-1][u-1] = d

    warshallfloyd(V,G)

    if any(G[i][i]<0 for i in range(V)):
        print("NEGATIVE CYCLE")
        return
