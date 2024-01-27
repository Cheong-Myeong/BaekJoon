def solution(my_string, overwrite_string, s):
    end_index = s + len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[end_index:]
    return answer