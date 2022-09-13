### http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=jp

from heapq import heappush, heappop, heapify

def prim(N, G):
    """
    N: Number of Nodes
    G: set of Edges
    """
    used = [0]*N
    que = [(c, w) for w, c in G[0]]
    used[0] = 1
    heapify(que)

    ans = 0
    while que:
        cv, v = heappop(que)
        if used[v]:
            continue
        used[v] = 1
        ans += cv
        for w, c in G[v]:
            if used[w]:
                continue
            heappush(que, (c, w))
            
    return ans

#-------------------------------

V, E = map(int, input().split())
G = [[] for _ in range(V)]
for i in range(E):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
        
print(prim(V, G))