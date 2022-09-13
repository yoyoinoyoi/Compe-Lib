"""
nCk をpで割った余りを求めるプログラム.
"""

n,k = map(int,input().split())
p = 10**9 + 7#素数

#オーソドックスな方法O(k)

def nCk_modp(n,k,p):
  nCk = 1
  for i in range(n-k+1,n+1):
    nCk = (nCk * i) % p
  for i in range(1,k+1):
    nCk = (nCk * pow(i,p-2,p)) % p
  return nCk
  
print(nCk_modp(n,k,p))

#ちょっと変わった方法O(n)

f = [1,1]
inv = [0,1]
f_inv = [1,1]
 
for i in range(2,n+1):
  inv_i = -inv[p%i]*(p//i)%p
  inv.append(inv_i)
  f_inv.append(inv_i*f_inv[i-1]%p)
  f.append(i*f[-1]%p)
  
print(f[n]*f_inv[k]*f_inv[n-k]%p)