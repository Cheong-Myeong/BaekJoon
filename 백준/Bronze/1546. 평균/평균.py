N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
result = 0
for num in lst:
    result += (num / M) * 100
print(result / N)