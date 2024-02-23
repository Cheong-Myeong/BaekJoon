N, M = map(int, input().split())
arr = [0] * N  # 바구니
for num in range(1, N + 1):
    arr[num-1] = num
for _ in range(M):
    i, j = map(int, input().split())
    ball1, ball2 = arr[i-1], arr[j-1]
    arr[i-1] = ball2
    arr[j-1] = ball1
print(*arr)