S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    if alphabet[i] in S:
        for idx, char in enumerate(S):
            if alphabet[i] == char:
                print(idx, end=' ')
                break
    else: print(-1, end=' ')