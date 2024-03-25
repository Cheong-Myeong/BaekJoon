import sys
input = sys.stdin.readline

M = int(input())  # 쿼리의 개수
A = 0             # A를 리스트로 하면 시간 초과. 바로 답 구할 수 있게 정수로 변경.
ans = 0
for _ in range(M):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        A += arr[1]       # 더하기
        ans ^= arr[1]     # A 원소 XOR
    elif arr[0] == 2:
        A -= arr[1]       # 빼기
        ans ^= arr[1]     # A 원소 XOR
    elif arr[0] == 3:
        print(A)          # A의 현재 값 출력
    elif arr[0] == 4:     # XOR을 여기서 for문 돌리니 시간 초과
        print(ans)        # A의 원소 들어가고 나갈 때 바로 해야함