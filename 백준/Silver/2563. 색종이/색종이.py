base = [[0]*100 for _ in range(100)]
N = int(input())    # 색종이 수
for _ in range(N):
    x, y = map(int, input().split())  # 색종이 왼쪽 아래 좌표 받기

    for i in range(x, x+10):   # 크기가 10인 정사각형 색종이를
        for j in range(y, y+10):
            base[i][j] = 1     # 면적만큼 1로 색칠
cnt = 0
for lst in base:
    cnt += lst.count(1)
print(cnt)