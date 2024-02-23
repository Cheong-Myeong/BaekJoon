arr = set()
for i in range(1, 31):
    arr = arr | {i}
for _ in range(28):
    j = int(input())
    arr = arr - {j}
num1 = arr.pop()
num2 = arr.pop()
if num1 > num2:
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)