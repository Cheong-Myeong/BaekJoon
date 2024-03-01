num1 = int(input())
max_len = 0
final_lst = []

def func(x, y):
    global lst
    while x - y >= 0:
        z = x - y
        lst.append(z)
        x, y = y, z
    return lst

for num2 in range(1, num1+1):
    lst = [num1, num2]
    current_lst = func(num1, num2)

    if max_len < len(current_lst):
        max_len = len(current_lst)
        final_lst = current_lst

print(len(final_lst))
print(*final_lst)