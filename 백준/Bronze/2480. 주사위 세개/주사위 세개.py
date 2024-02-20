A, B, C = map(int, input().split())

if A == B == C:
    print(10000+A*1000)

if A == B and A != C:
    print(1000+A*100)
elif B == C and B != A:
    print(1000+B*100)
elif C == A and C != B:
    print(1000+C*100)

if A != B and B != C and C != A:
    print(max([A, B, C])*100)