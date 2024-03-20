from collections import deque

def bfs(r, c, cnt):
    q = deque([(r, c, cnt)])  # 큐 삽입
    while q:  # q가 비워질 때까지
        r, c, cnt = q.popleft()
        arr[r][c] = 0   # 벽체크 때 중복 방지
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 벽체크
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1 and result[nr][nc] == 0:
                result[nr][nc] = cnt  # 거리 입력
                q.append((nr, nc, cnt + 1))

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

n, m = map(int, input().split())  # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * m for _ in range(n)]
flag = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:  # 시작 위치를 찾으면
            bfs(i, j, 1)    # 간선 거리 구하기
            flag = 1
            break
    if flag:
        break

for x in range(n):
    for y in range(m):
        if arr[x][y] == 1 and result[x][y] == 0:  # 1인데 방문하지 못한 곳은 -1 출력
            print(-1, end=' ')
        else:
            print(result[x][y], end=' ')
    print()