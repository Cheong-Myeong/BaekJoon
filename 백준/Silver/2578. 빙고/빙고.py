bingo = [list(map(int, input().split())) for _ in range(5)]  # 내 빙고판
number = []  # 사회자가 부르는 수
for _ in range(5):
    a, b, c, d, e = map(int, input().split())
    lst = [a, b, c, d, e]
    number += lst

def mark(num):  # 사회자가 부르는 수 핑고판에 표시
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number[num]:
                bingo[i][j] = 0
    return bingo

num = 0  # 사회자가 부르는 횟수
cnt = 0  # 빙고 세기
while num < 25:
    mark(num)
    num += 1
    # 가로줄이 빙고인지 확인
    for width in bingo:
        if width[0] == 0 and width[1] == 0 and width[2] == 0 and width[3] == 0 and width[4] == 0:
            cnt += 1
    # 대각선이 빙고인지 확인
    if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0 and bingo[3][3] == 0 and bingo[4][4] == 0:
        cnt += 1
    if bingo[0][4] == 0 and bingo[1][3] == 0 and bingo[2][2] == 0 and bingo[3][1] == 0 and bingo[4][0] == 0:
        cnt += 1
    # 세로줄이 빙고인지 확인
    if bingo[0][0] == 0 and bingo[1][0] == 0 and bingo[2][0] == 0 and bingo[3][0] == 0 and bingo[4][0] == 0:
        cnt += 1
    if bingo[0][1] == 0 and bingo[1][1] == 0 and bingo[2][1] == 0 and bingo[3][1] == 0 and bingo[4][1] == 0:
        cnt += 1
    if bingo[0][2] == 0 and bingo[1][2] == 0 and bingo[2][2] == 0 and bingo[3][2] == 0 and bingo[4][2] == 0:
        cnt += 1
    if bingo[0][3] == 0 and bingo[1][3] == 0 and bingo[2][3] == 0 and bingo[3][3] == 0 and bingo[4][3] == 0:
        cnt += 1
    if bingo[0][4] == 0 and bingo[1][4] == 0 and bingo[2][4] == 0 and bingo[3][4] == 0 and bingo[4][4] == 0:
        cnt += 1

    # 3줄 빙고되면 출력, 그렇지 않으면 while문 반복
    if cnt >= 3:
        print(num)
        break
    else:
        cnt = 0  # 빙고를 다시 세기 때문에 0으로 초기화
        continue