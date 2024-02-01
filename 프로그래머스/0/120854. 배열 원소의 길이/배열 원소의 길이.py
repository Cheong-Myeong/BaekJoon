def solution(strlist):
    answer = []
    for text in strlist:
        cnt = 0
        for _ in text:
            cnt += 1
        answer.append(cnt)    
    return answer