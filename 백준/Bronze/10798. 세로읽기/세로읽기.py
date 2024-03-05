string_lst = []
max_len = 0
for i in range(5):
    string_lst.append(list(map(str, input())))
    if max_len < len(string_lst[i]):
        max_len = len(string_lst[i])

for idx in range(max_len):  # 가장 긴 글자의 길이만큼 반복하되
    for j in range(5):      
        try:                
            print(string_lst[j][idx], end='')

        except IndexError:  # 그보다 짧은 글자라서 error가 나면 pass하고
            pass            # 다음 글자의 같은 idx 원소 출력