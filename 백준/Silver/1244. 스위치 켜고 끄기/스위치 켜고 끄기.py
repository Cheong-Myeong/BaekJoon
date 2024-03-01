N = int(input())  # 스위치 개수
lst = list(map(int, input().split()))  # 스위치 상태
M = int(input())  # 학생 수
student_lst = [list(map(int, input().split())) for _ in range(M)]  # 성별, 번호

def switch(idx):  # 스위치 상태 반대로 바꾸기 함수
    if lst[idx]:
        lst[idx] = 0
    else:
        lst[idx] = 1
    return lst[idx]

for gender, number in student_lst:
    if gender == 1:                     # 남학생이면
        for j in range(1, N+1):
            if j % number == 0:         # 스위치 번호가 배수일 때
                switch(j-1)             # 스위치 상태 반대로 바꾸기

    else:                               # 여학생이면
        my_idx = number - 1             # 여학생 번호표 스위치 idx
        min_idx = 0                     # 벽 체크 인덱스 변수
        if N - (1 + my_idx) >= my_idx:  # my_idx와 양 끝을 비교
            min_idx = my_idx
        else:
            min_idx = N - (1 + my_idx)

        for k in range(1, min_idx + 1):
            left = my_idx - k                 # 왼쪽 탐색 idx
            right = my_idx + k                # 오른쪽 탐색 idx
            if lst[left] == lst[right]:       # 대칭이면 바꾸기
                switch(left)
                switch(right)
            else: break                 # 대칭이 아니면 빠져나오기
        switch(my_idx)                  # 여학생 번호표 스위치 바꾸기

H = len(lst)
for lst_idx in range(1, H+1):
    print(lst[lst_idx-1], end=' ')
    if lst_idx % 20 == 0:               # 한 줄에 20개씩 출력
        print()
