def solution(my_string, letter):
    answer = ''
    for txt in my_string:
        if txt != letter:
            answer += txt
    return answer