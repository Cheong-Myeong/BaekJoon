w, h = map(int, input().split())  # 가로, 세로 길이
p, q = map(int, input().split())  # 시작 위치 좌표
t = int(input())                  # 개미가 움직이는 시간

p_lst, q_lst = [], []  # 개미가 움직이는 좌표 리스트
for i in range(1, w):  # 초기 위치가 1이상이라서 범위 시작을 1부터
    p_lst.append(i)    # [1, 2, 3, 4, 5]
for j in range(1, h):
    q_lst.append(j)    # [1, 2, 3]

for i in range(w, -1, -1):
    p_lst.append(i)    # [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]
for j in range(h, -1, -1):
    q_lst.append(j)    # [1, 2, 3, 4, 3, 2, 1, 0]

x = p_lst[(p+t-1) % len(p_lst)]
y = q_lst[(q+t-1) % len(q_lst)]

print(x, y)