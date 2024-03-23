import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 재귀의 최대 깊이 설정

def bossfind(x):
    if boss[x] != x:
        boss[x] = bossfind(boss[x])
    return boss[x]

def union(x, y):
    x = bossfind(x)
    y = bossfind(y)
    if x < y:   # 다른 집합이면 작은 수로 합침
        boss[y] = x
    else:
        boss[x] = y

n, m = map(int, input().split())
boss = [i for i in range(n+1)]

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    else:
        if bossfind(a) == bossfind(b):
            print('YES')
        else:
            print('NO')