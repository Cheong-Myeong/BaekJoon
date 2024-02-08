def solution(arr):
    answer = []
    for num in arr:
        if num >= 50 and num % 2 == 0:
            answer += [num // 2]
        elif num < 50 and num % 2 == 1:
            answer += [num * 2]
        else:
            answer += [num]
    
    return answer