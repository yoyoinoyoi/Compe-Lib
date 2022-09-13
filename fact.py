# fact(n) -> list
def pl(n):
  a = []
  while n % 2 == 0:
    a.append(2)
    n //= 2
  f = 3
  while f**2 <= n:
    if n % f == 0:
      a.append(f)
      n //= f
    else:
      f += 2
  if n != 1:
    a.append(n)
  return a

# fact(n) -> set
def ps(n):
  a = set()
  while n % 2 == 0:
    a.add(2)
    n //= 2
  f = 3
  while f**2 <= n:
    if n % f == 0:
      a.add(f)
      n //= f
    else:
      f += 2
  if n != 1:
      a.add(n)
  return a
  
# fact(n) -> dict
def pd(n):
  a = {}
  while n % 2 == 0:
    if 2 not in a:
      a[2] = 1
    else:
      a[2] += 1
    n //= 2
  f = 3
  while f**2 <= n:
    if n % f == 0:
      if f not in a:
        a[f] = 1
      else:
        a[f] += 1
      n //= f
    else:
      f += 2
  if n != 1:
    if n not in a:
      a[n] = 1
    else:
      a[n] += 1
  return a

N = int(input())
print(pl(N))
print(ps(N))
print(pd(N))