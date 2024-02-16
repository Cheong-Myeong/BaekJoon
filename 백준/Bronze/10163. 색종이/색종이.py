N = int(input()) # 색종이의 수
arr = [[0]*101 for _ in range(101)] # 색종이가 놓이는 평면

# 주어지는 순서대로 색종이 좌표 받고 면적 표시
mark = 0
for _ in range(N):
    # i1 j1 가장 왼쪽 아래 칸의 번호, i2 너비, j2 높이
    i1, j1, i2, j2 = map(int, input().split())
    # 색종이마다 면적 표시하는 값을 다르게 줌
    mark += 1
    for i in range(i1, i1 + i2):       # 행 좌표
        for j in range(j1, j1 + j2):   # 열 좌표
            arr[i][j] = mark

# 주어진 순서대로 색종이 면적 출력
for j in range(1, N+1):
    cnt = 0
    for lst in arr:
        cnt += lst.count(j)
    print(cnt)