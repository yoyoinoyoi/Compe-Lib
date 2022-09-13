#ABC103 Island War

N,M = map(int,input().split())
for i in range(M):
  sec = [list(map(int,input().split())) for _ in range(M)]
  sec = sorted(sec,reverse=True)
  sec = sorted(sec,key=lambda x: x[1])

ans = 0
t = 0
for i in range(N):
  if (t < sec[i][1]):
    ans += 1
    t = sec[i][[0]]

print(ans)