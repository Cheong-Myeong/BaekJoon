my_set = set()
for _ in range(10):
    N = int(input())
    my_set.add(N % 42)
print(len(my_set))