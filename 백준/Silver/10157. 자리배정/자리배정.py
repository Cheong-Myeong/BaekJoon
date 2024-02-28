C, R = map(int, input().split())  # C 가로, R 세로
K = int(input())                  # 대기 번호
base = [[0] * R for _ in range(C)]

dr = [0, 1, 0, -1]                # 오른, 아래, 왼, 위
dc = [1, 0, -1, 0]

k = 1
d = 0                             # 네방향 탐색에 사용
nr, nc = 0, 0                     # 시작 좌표
base[nr][nc] = k                  # 시작 칸에 1 채우기

# 네방향 탐색 (한 방향 가다가 막히면 다음 방향)
while k < C * R:
    nr += dr[d % 4]
    nc += dc[d % 4]
    if 0 <= nr < C and 0 <= nc < R and base[nr][nc] == 0:  # 벽체크
        k += 1
        base[nr][nc] = k          # 대기번호 기입
    else:
        nr -= dr[d % 4]           # 벽 뚫으면 이전 좌표로 돌림
        nc -= dc[d % 4]
        d += 1

row, col = 0, 0
for i in range(C):
    for j in range(R):
        if base[i][j] == K:
            row, col = i+1, j+1

if K > R * C:   # row == 0 and col == 0: 이 조건도 가능
    print(0)
else:
    print(row, col)