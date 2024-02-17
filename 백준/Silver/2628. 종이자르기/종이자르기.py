width, height = map(int, input().split())  # 종이의 가로, 세로 길이
N = int(input())    # 자르는 횟수
lst = [list(map(int, input().split())) for _ in range(N)]

width_lst = [0]  # 0은 첫 좌표
height_lst = [0]
# 가로 / 세로 자르는 점선 좌표 구분해서 리스트 넣기
for lst1 in lst:
    if lst1[0] == 0:
        height_lst += [lst1[1]]
    if lst1[0] == 1:
        width_lst += [lst1[1]]

# 리스트 오름차순 정렬 후 마지막 좌표(종이의 길이) 추가
width_lst.sort()
width_lst.append(width)
height_lst.sort()
height_lst.append(height)

# 가로 좌표끼리의 거리 중 최대값 찾기
width_max = 0
for i in range(len(width_lst)-1):
    if width_max < width_lst[i+1] - width_lst[i]:
        width_max = width_lst[i+1] - width_lst[i]
# 세로 좌표끼리의 거리 중 최대값 찾기
height_max = 0
for j in range(len(height_lst)-1):
    if height_max < height_lst[j+1] - height_lst[j]:
        height_max = height_lst[j+1] - height_lst[j]

print(width_max * height_max)