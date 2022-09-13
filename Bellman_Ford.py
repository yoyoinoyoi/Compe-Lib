# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp

def bellman_ford(N, G, s):
    """bellman_ford

    Args:
        N (int): number of nodes
        G[v] (int w, int c): w reachable at cost c from v
        s (int): start position (0, ..., N-1)

    Returns:
        if negative closed circuit exists: -1
        else: 
            dist[v]: Minimum cost from start to v
    """
    INF = float('inf')
    dist = [INF] * N
    dist[s] = 0
    for i in range(N):
        update = False
        for v, e in enumerate(G):
            for t, cost in e:
                if dist[v] + cost < dist[t]:
                    dist[t] = dist[v] + cost
                    update = True
        if not update:
            break
        if i == N -1:
            print("NEGATIVE CYCLE")
            return
    for s in dist:
        if s == INF:
            print("INF")
        else:
            print(s)
    return

# -----------------------------------

V, E, r = map(int, input().split())
G = [[] for _ in range(V)]
for j in range(E):
    s, t, d = map(int, input().split())
    G[s].append([t, d])
    
bellman_ford(V, G, r)