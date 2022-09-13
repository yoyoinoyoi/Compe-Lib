### http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=jp

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # union x-y
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # find x's root
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

def Kruskal(N, G):
    uf = UnionFind(N)
    ans = 0
    for x, y, cost in G:
        if uf.find(x) != uf.find(y):
            uf.union(x, y)
            ans += cost
    return ans

#-----------------------------------

V, E = map(int, input().split())
G = []
for i in range(E):
    a, b, c = map(int, input().split())
    G.append((a, b, c))
    G.append((b, a, c))

G.sort(key = lambda x:x[2])
print(Kruskal(V, G))