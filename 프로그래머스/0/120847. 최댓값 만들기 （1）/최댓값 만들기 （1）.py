def solution(numbers):
    # numbers 원소 개수 카운트
    N = 0
    for _ in numbers:
        N += 1
    # numbers 오름차순 정렬    
    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1]  = numbers[j+1], numbers[j]
    print(numbers)            
    # numbers 첫번째 큰 값 * 두번째 큰 값
    answer = numbers[N-1] * numbers[N-2]
    return answer