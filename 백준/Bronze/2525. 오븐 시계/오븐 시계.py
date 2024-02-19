H, M = map(int, input().split())
plus = int(input())
minute = M + plus

if minute >= 60:
    print((H+(minute//60))%24, (minute-60*(minute//60)))
elif minute < 60:
    print(H, minute)