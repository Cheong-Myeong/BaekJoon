arr = []
for _ in range(9):
    arr.append(int(input()))

max_v = 0
for num in arr:
    if max_v < num:
        max_v = num
print(max_v)

for i in range(9):
    if max_v == arr[i]:
        print(i+1)