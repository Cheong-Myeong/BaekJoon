N = int(input())
lst = list(map(int, input().split()))
big_cnt = 1  # 연속해서 커질 때마다 cnt (최소 길이 1)
small_cnt = 1  # 연속해서 작아질 때마다 cnt (최소 길이 1)
big_cnts = [1]
small_cnts = [1]

for idx in range(N - 1):
    if lst[idx] <= lst[idx + 1]:  # 연속해서 같거나 커질 때
        big_cnt += 1
    else:
        big_cnts.append(big_cnt)
        big_cnt = 1  # 초기화

    if lst[idx] >= lst[idx + 1]:  # 연속해서 같거나 작아질 때
        small_cnt += 1
    else:
        small_cnts.append(small_cnt)
        small_cnt = 1  # 초기화

    if idx == N - 2:
        big_cnts.append(big_cnt)
        small_cnts.append(small_cnt)

print(max(max(big_cnts), max(small_cnts)))