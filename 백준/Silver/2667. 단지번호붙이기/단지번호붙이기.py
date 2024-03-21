from collections import deque

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    deque.append(q, (x, y))
    house_cnt = 1
    while q:
        x, y = deque.popleft(q)
        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            # 벽체크
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                # visited[nr][nc] = 1
                house_cnt += 1
                deque.append(q, (nr, nc))
    return house_cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# visited = [[0] * N for _ in range(N)]
cnt = 0
house_cnt_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = 0
            # visited[i][j] = 1
            house_cnt_lst.append(bfs(i, j))
            cnt += 1

print(cnt)
house_cnt_lst.sort()
for num in house_cnt_lst:
    print(num)