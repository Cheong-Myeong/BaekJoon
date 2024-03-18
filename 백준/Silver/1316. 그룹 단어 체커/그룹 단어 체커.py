n = int(input())
cnt = n
for _ in range(n):
    word = input()
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있다면
                cnt -= 1  # cnt에 1씩 감소.
                break
print(cnt)