M = int(input())  # M <= N
N = int(input())
final_lst = []    # M ~ N 중 소수 리스트

for i in range(M, N+1):
    current_lst = []              # M ~ N의 약수 리스트
    for j in range(1, i+1):
        if i % j == 0:            # j가 i의 약수일 때
            current_lst.append(i // j)

        if len(current_lst) > 2:  # 약수가 3개 이상이면 멈춤(가지치기)
            break
    if len(current_lst) == 2:     # for문을 다 돌아도 약수가 2개이면
        final_lst.append(i)       # 소수 리스트에 추가

if len(final_lst) > 0:
    print(sum(final_lst))
    print(min(final_lst))
else: print(-1)