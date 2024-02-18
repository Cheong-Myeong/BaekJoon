lst = []
for _ in range(2):
    value = int(input())
    lst.append(value)

if lst[0] > 0:
    if lst[1] > 0:
        print(1)
    else:
        print(4)
elif lst[0] < 0:
    if lst[1] > 0:
        print(2)
    else:
        print(3)