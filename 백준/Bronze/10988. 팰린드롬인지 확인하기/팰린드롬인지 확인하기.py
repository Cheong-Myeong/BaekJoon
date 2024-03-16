string = input()
n = len(string)
start, end = 0, n-1
flag = 1
while start < end:
    if string[start] == string[end]:
        start += 1
        end -= 1
        pass
    else:
        flag = 0
        break
print(flag)