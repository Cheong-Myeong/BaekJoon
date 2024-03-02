A, B = map(int, input().split())
A_reverse = ''
B_reverse = ''

for _ in range(3):
    num = A % 10
    A_reverse += str(num)
    A = A // 10

for _ in range(3):
    num = B % 10
    B_reverse += str(num)
    B = B // 10

if int(A_reverse) > int(B_reverse):
    print(A_reverse)
else:
    print(B_reverse)