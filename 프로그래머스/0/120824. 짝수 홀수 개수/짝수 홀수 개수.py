def solution(num_list):
    cnt1 = cnt2 = 0
    for num in num_list:
        if num % 2 == 0:
            cnt1 += 1
        else:
            cnt2 += 1
    answer = [cnt1, cnt2]
    return answer