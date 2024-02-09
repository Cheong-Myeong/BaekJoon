def solution(n, k):
    answer = []
    for i in range(1, n//k+1):
        if k * i <= n:
            answer += [k * i]
        
    return answer