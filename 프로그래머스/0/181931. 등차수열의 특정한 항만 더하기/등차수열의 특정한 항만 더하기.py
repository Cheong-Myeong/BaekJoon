def solution(a, d, included):
    n = len(included)
    lst = [a]
    #lst에 첫째항 a의 공차가 d인 리스트 만들기 (included 길이만큼)
    for _ in included[1:n]:
        a += d
        lst.append(a)
        
    # included의 i인덱스가 true일 때 lst의 i인덱스 더하기 
    answer = 0
    for i in range(n):
        if included[i]:
            answer += lst[i]
         
    return answer