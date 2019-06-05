#二部グラフの判定、codefestival2017 C問題3-stepsでverify
N,M = map(int,input().split())
G = defaultdict(set)
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].add(b-1)
    G[b-1].add(a-1)
"""
colorグループを外で持ちたいとき
color = [0 for i in range(len(G))]
color[0]=1
"""
#二部グラフであるかの判定
def Isbipartite(G):
    color = [[0] for i in range(len(G))]
    color[0]=1
    que=deque([0])
    bipartite = True
    while que:
        p = que.popleft()
        for q in list(G[p]):
            if color[q]==0:
                color[q] = -color[p]
                que.append(q)
            elif color[q] == color[p]:
                bipartite = False
                break
    return bipartite


if Isbipartite(G):
    print(color.count(1)*color.count(-1)-M)
else:
    print(N*(N-1)//2-M)
