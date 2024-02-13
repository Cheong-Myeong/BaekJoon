N = int(input()) # 학생 수
arr = list(map(int, input().split())) # 번호표

# 첫번째 학생은 무조건 제일 앞에 줄 섬
lst = [1]

# 두번째 학생부터 마지막 학생까지
for i in range(2, N+1):
    # 해당 학생의 번호표 n
    n = arr[i-1]
    # 해당 학생이 들어갈 자리 lst[i-1-n]
    lst.insert(i-1-n, i)

print(' '.join(map(str, lst)))