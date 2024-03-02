T = int(input())
for tc in range(1, T+1):
    R, S = map(str, input().split())
    for char in S:
        print(char * int(R), end='')
    print()