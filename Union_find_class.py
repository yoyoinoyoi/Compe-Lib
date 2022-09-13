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

    # tree size including x
    def size(self, x):
        return -self.parents[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

#ABC177D Friends
N,M = map(int,input().split())
parents = [-1]*N
uf = UnionFind(N)
for i in range(M):
    A,B = map(int,input().split())
    uf.union(A-1,B-1)

ans = 0
for i in range(N):
    ans = max(ans,uf.size(i))

print(ans)