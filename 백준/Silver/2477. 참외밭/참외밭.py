K = int(input())
arr = []

ew_max, sn_max = 0, 0  # 가로(동서 빙향), 세로(남북 방향) 최대값 구하기
ew_idx, sn_idx = 0, 0  # 최대값의 arr 인덱스 구하기
for i in range(6):
    a, b = map(int, input().split())
    arr.append([a, b])
    if arr[i][0] == 1 or arr[i][0] == 2:  # 동서 방향일 때
        if ew_max < arr[i][1]:
            ew_max = arr[i][1]
            ew_idx = i
    else:                                 # 남북 방향일 때
        if sn_max < arr[i][1]:            
            sn_max = arr[i][1]
            sn_idx = i

max_value = ew_max * sn_max      # 최대 넓이

if ew_idx == 0 or sn_idx == 0:   # 최대값과 인접한 리스트 원소 길이 0으로 바꾸기
    arr[1][1], arr[5][1] = 0, 0
if ew_idx == 5 or sn_idx == 5:
    arr[0][1], arr[4][1] = 0, 0
if 1 <= ew_idx <= 4:
    arr[ew_idx-1][1], arr[ew_idx+1][1] = 0, 0
if 1 <= sn_idx <= 4:
    arr[sn_idx - 1][1], arr[sn_idx + 1][1] = 0, 0

value = 1
for j in range(6):
    if arr[j][1]:                # 원소 길이가 0이 아니면(최대값과 인접하지 않으면)
        value *= arr[j][1]       # 남아있는 리스트 원소끼리 곱 구하기

print((max_value - value) * K)