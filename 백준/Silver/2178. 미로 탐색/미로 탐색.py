def bfs(r, c):
    q = []
    # 큐 삽입
    q.append((r, c))
    while q:  # q가 비워질 때까지
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 벽체크
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                q.append([nr, nc])
    return arr[N-1][M-1]

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
sr, sc = 0, 0
print(bfs(sr, sc))