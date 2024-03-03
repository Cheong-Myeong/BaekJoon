# 입력 받기
lines = []
while True:
    try:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    except EOFError:
        break

# 입력 받은 대로 출력
for line in lines:
    print(line)