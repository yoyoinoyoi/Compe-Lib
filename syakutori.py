N,K = map(int, input().split())
A = list(map(int, input().split()))

def cond(m,a,K):#条件
  return m + A[r] < K
 
ans,r,m = 0,0,0
for l in range(N):
  while (r < N) and cond(m,A[r],K):
    m += A[r]
    r += 1
    
  ans += N-r
  if r == l:
    r += 1
  else:
    m -= A[l]
    
print(ans)

#ABC130 Enough_Array