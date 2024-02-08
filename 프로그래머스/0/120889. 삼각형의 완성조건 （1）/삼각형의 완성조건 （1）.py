def solution(sides):
    # 오름차순 정렬
    for i in range(2, 0, -1):
        for j in range(0, i):
            if sides[j] > sides[j+1]:
                sides[j], sides[j+1] = sides[j+1], sides[j]
    # 가장 큰 수와 나머지 원소 합 비교
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    else:
        answer = 2
        
    return answer   