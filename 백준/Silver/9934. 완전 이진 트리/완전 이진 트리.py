def func(lst, level):
    global ans
    N = len(lst)
    ans[level].append(lst[N//2])

    if N == 1:
        return

    left = lst[:(N//2)]
    right = lst[(N//2)+1:]

    func(left, level + 1)
    func(right, level + 1)


K = int(input())  # 트리의 깊이
arr = list(map(int, input().split()))
ans = [[] for _ in range(K)]  # 깊이 수만큼 이차원 리스트 만들기
func(arr, 0)
for answer in ans:
    print(*answer)