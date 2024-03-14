for test_case in range(4):
    x1, y1, x2, y2, p1, q1, p2, q2 = map(int, input().split())
    width_cnt, height_cnt = -1, -1

    if x1 <= p1 <= x2:  # 첫번째 사각형 가로 범위에 두번째 사각형 가로 시작 지점이 포함된다면
        width_cnt += x2 - p1 + 1  # 포함되는 범위만큼 count
    if p1 <= x1 <= p2:
        width_cnt += p2 - x1 + 1
    if y1 <= q1 <= y2:  # 첫번째 사각형 세로 범위에 두번째 사각형 세로 시작 지점이 포함된다면
        height_cnt += y2 - q1 + 1
    if q1 <= y1 <= q2:
        height_cnt += q2 - y1 + 1

    if width_cnt == -1 or height_cnt == -1:  # 포함된 범위가 없다면
        print('d')
    elif width_cnt == 0 and height_cnt == 0:  # 포함된 범위가 가로, 세로 모두 한 지점뿐이라면
        print('c')
    elif width_cnt > 0 and height_cnt > 0:  # 포함된 범위가 가로, 세로 모두 한 지점 초과라면
        print('a')
    else:  # 포함된 범위가 가로, 세로 중 한 곳은 한 지점뿐이고, 다른 부분은 한 지점 초과라면
        print('b')