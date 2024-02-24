N, K = map(int, input().split())  # N 리스트 길이, K 합을 구하는 길이
lst = list(map(int, input().split()))

max_v = sum(lst[:K])         # K씩 묶어서 구한 합 중 최대값 저장 변수
value = sum(lst[:K])         # K씩 묶어서 구한 합
for i in range(K, N):
    value += lst[i] - lst[i-K]
    if max_v < value:
        max_v = value
print(max_v)