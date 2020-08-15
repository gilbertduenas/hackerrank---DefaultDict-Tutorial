# i'm no genius, but i can understand when one speaks.
from collections import defaultdict

a = defaultdict(list)
n, m = map(int, input().split())

for i in range(n):
    a[input()].append(str(i+1))

for i in range(m):
    print(' '.join(a[input()]) or -1)
