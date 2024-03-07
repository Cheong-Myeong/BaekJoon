N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N  # 자신도 길이에 포함이므로 기본값은 1
for i in range(1, N):
    for j in range(0, i):    # 0부터 자신 앞까지 원소 중에
        if arr[j] < arr[i]:  # 자기보다 값이 작으면
            dp[i] = max(dp[i], dp[j]+1)  # dp값 업데이트
print(max(dp))