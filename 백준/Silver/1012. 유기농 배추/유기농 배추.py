dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = [(r, c)]  # 큐 삽입
    while q:  # q가 비워질 때까지
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 벽체크
            if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 1:
                arr[nr][nc] = 0  # 다음 위치 0으로 바꾸기
                q.append((nr, nc))

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # 가로, 세로, 배추의 개수
    arr = [[0] * N for _ in range(M)]    # 반대로...? M, N 바뀌어야 함
    # arr에 배추 심기
    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1
    # 배추 위치이면 cnt += 1
    cnt = 0
    for r in range(M):
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
                bfs(r, c)  # 인접한 곳이 1이면 0으로 바꿈
    print(cnt)