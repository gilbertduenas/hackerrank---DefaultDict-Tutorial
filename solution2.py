# used a list comprehension
from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)

for i in range(n):
  a[input()].append(i+1)

b = [input() for i in range(m)]

for i in b: 
  if i in a:
    print(' '.join(map(str, a[i])))
  else:
    print(-1)
