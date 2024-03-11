N, K = map(int, input().split())
arr = [i for i in range(2, N+1)]  # 2부터 N까지 리스트
cnt, result = 0, 0  # cnt 지우는 횟수, result cnt에 해당하는 수
flag = 0
for j in range(len(arr)):    # arr 길이만큼 돌면서
    if arr[j]:               # arr[j]가 0이 아니라면
        min_v = arr[j]       # min_v 지우지 않은 가장 작은 수
        result = arr[j]
        arr[j] = 0           # 0으로 지우기
        cnt += 1
        n = 0
        while n < len(arr):  # arr 길이만큼 돌면서
            if arr[n] != 0 and arr[n] % min_v == 0:
                result = arr[n]
                arr[n] = 0   # 아직 지우지 않은 min_v의 배수 지우기
                n += 1
                cnt += 1
            else:
                n += 1
            if cnt == K:     # K번째 지우는 횟수가 되면 반복문 중지
                flag = 1
                break
    if flag:
        break
print(result)