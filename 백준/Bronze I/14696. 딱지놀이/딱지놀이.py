N = int(input()) # 라운드 수
# arr = 라운드 별 A/B의 딱지모양
arr = [list(map(int, input().split())) for _ in range(N*2)]

# arr의 짝수 요소는 A의 딱지모양 / 홀수는 B의 딱지모양
for i in range(N):
    A_lst = arr[2*i]
    B_lst = arr[2*i+1]

    # A/B의 딱지모양 별 cnt
    A_cnt_4 = A_lst.count(4)
    B_cnt_4 = B_lst.count(4)
    A_cnt_3 = A_lst.count(3)
    B_cnt_3 = B_lst.count(3)
    A_cnt_2 = A_lst.count(2)
    B_cnt_2 = B_lst.count(2)
    A_cnt_1 = A_lst.count(1)
    B_cnt_1 = B_lst.count(1)

    # 승부 가리기
    if A_cnt_4 != B_cnt_4:
        if A_cnt_4 > B_cnt_4:
            print('A')
        else:
            print('B')
    elif A_cnt_4 == B_cnt_4 and A_cnt_3 != B_cnt_3:
        if A_cnt_3 > B_cnt_3:
            print('A')
        else:
            print('B')
    elif A_cnt_4 == B_cnt_4 and A_cnt_3 == B_cnt_3 and A_cnt_2 != B_cnt_2:
        if A_cnt_2 > B_cnt_2:
            print('A')
        else:
            print('B')
    elif A_cnt_4 == B_cnt_4 and A_cnt_3 == B_cnt_3 and A_cnt_2 == B_cnt_2 and A_cnt_1 != B_cnt_1:
        if A_cnt_1 > B_cnt_1:
            print('A')
        else:
            print('B')
    else:
        print('D')