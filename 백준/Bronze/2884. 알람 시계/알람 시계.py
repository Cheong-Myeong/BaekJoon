H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
elif M < 45:
    print((H+23) % 24, 60-(45-M))