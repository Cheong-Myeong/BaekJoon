import sys
input = sys.stdin.readline

def func(ans):
    global visited
    if len(ans) == M:  # 리스트 길이가 M이 되면 출력
        print(*ans)
        return

    for i in range(0, N):
        if visited[i] == 0:  # 방문체크
            visited[i] = 1
            ans.append(i+1)
            func(ans)
            ans.pop()        # 재귀가 끝나면 pop, 방문 풀기
            visited[i] = 0

N, M = map(int, input().split())
visited = [0] * N
func([])