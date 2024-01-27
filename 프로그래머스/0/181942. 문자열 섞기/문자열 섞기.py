def solution(str1, str2):
    answer = ''
    for num in range(len(str1)):
        answer = answer + str1[num] + str2[num] 
    return answer