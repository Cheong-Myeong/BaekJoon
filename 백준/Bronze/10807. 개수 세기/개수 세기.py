N = int(input())
arr = list(map(int, input().split()))
V = int(input())

cnt = 0
for i in arr:
    if V == i:
        cnt += 1

print(cnt)