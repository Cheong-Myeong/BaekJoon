def solution(numbers):
    cnt = num_sum = 0
    for num in numbers:
        cnt += 1
        num_sum += num
    answer = num_sum / cnt 
    return answer