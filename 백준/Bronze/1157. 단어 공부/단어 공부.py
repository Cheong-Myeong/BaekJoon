string = input().upper()   # 출력하기 쉽게 모두 대문자로 바꾸기
char_string = list(set(string))  # 중복제거
cnt_lst = []

for char in char_string:  # 알파벳마다 개수 구하기
    cnt_lst.append(string.count(char))

max_cnt = max(cnt_lst)  # 가장 많이 사용된 개수
max_idx = cnt_lst.index(max_cnt)  # 그 개수의 인덱스 구하기

if cnt_lst.count(max_cnt) == 1:  # 가장 많이 사용된 알파벳이 하나이면
    print(char_string[max_idx])
else:
    print('?')