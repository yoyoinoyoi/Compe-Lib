#TDPC ターゲット
N = int(input())
A = []
for i in range(N):
    x,r = map(int,input().split())
    A.append([x-r,x+r])
inf = 10**12
dp = [inf]*N
A.sort(key=lambda x:x[0],reverse=True)
A.sort(key=lambda x:x[1],reverse=True)
#print(A)

def is_ok(p,n):
    return dp[n] >= p

def m_bisect(ng, ok, p):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(p, mid):
            ok = mid
        else:
            ng = mid
    return ok


for x,y in A:
    t = m_bisect(-1,N,x)
    dp[t] = x
    #print(dp)

ans = m_bisect(-1,N,inf-1)
print(ans)