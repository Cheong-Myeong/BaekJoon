def solution(n):
    if n % 2 == 1:
        answer = 0
        for num in range(n+1):
            if num % 2 == 1: 
                answer = answer + num
    else:
        answer = 0
        for num in range(n+1):
            if num % 2 == 0:
                answer = answer + num ** 2
    
    return answer