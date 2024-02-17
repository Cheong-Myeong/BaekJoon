base = [[0] * 100 for _ in range(100)]

for _ in range(4):   # 색종이 좌표 받기
    i1, j1, i2, j2 = map(int, input().split())
    
    for i in range(i1, i2):   # 색종이 면적만큼 1로 색칠
        for j in range(j1, j2):
            base[i][j] = 1
cnt = 0
for lst in base:   # 1로 색칠한 면적 출력
    cnt += lst.count(1)
print(cnt)