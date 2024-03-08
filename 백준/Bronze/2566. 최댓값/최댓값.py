arr = [list(map(int, input().split())) for _ in range(9)]
max_v = 0
r, c = 1, 1
for i in range(9):
    for j in range(9):
        if max_v < arr[i][j]:
            max_v = arr[i][j]
            r, c = i+1, j+1
print(max_v)
print(r, c)