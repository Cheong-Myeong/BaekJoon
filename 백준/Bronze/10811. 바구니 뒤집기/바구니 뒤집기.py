N, M = map(int, input().split())
arr = [0] * N  # 바구니
result = [0] * N  # 바구니
for num in range(1, N + 1):
    arr[num-1] = num
    result[num-1] = num

for _ in range(M):
    i, j = map(int, input().split())
    cnt = 0
    for k in range(i-1, j):
        result[k] = arr[j-cnt-1]
        cnt += 1
    arr = result[:]
print(*result)