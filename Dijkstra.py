#ARC treasure hunt
from heapq import heappop,heappush
from collections import deque

# Settings
inf = float('inf')
# const > N
const = 10**12

def dijkstra(N, G, s):
    dist = [inf] * N
    # already packing
    que = [s]
    dist[s] = 0
    before_pos = [-1]*N
    while que:
        c, v = unpack(heappop(que))
        if dist[v] < c:
            continue
        for gv in G[v]:
            t, cost = unpack(gv)
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, pack(dist[t], t))
                before_pos[t] = v

    # route を求める
    # Route[i]: path from start to node[i]
    Route = []
    for i in range(N):
        route = deque([i])
        pos = before_pos[i]
        while pos != -1:
            route.appendleft(pos)
            pos = before_pos[pos]
        Route.append(route)

    return dist, Route

def pack(a, b):
    return a*const +b

def unpack(v):
    return v//const, v%const

#-------------------

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
path1 = [[] for _ in range(N)]
path2 = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    # print(Map)
    path1[a-1].append(pack(b-1, c))
    path2[b-1].append(pack(a-1, c))

p0 = dijkstra(N, path1, 0)
pi = dijkstra(N, path2, 0)
ans = 0
for i in range(N):
    Time = p0[i] + pi[i]
    ans = max(ans, A[i] *(T -Time))

print(ans)