# 일곱 난장이 키 합 구하기
def f(arr):
    for i in arr:
        for j in arr:
            # arr에서 원소 2개 빼기
            if i != j:
                value = sum(arr) - (i + j)
                # arr에 있는 7개 원소의 합이 100이라면 반환
                if value == 100:
                    arr.remove(i)
                    arr.remove(j)
                    arr.sort()
                    return arr

# 아홉 난쟁이 키 리스트에 담기
arr = []
for _ in range(9):
    arr += [int(i) for i in input().split()]
    
# 출력
Arr = f(arr)
for num in range(7):
    print(Arr[num], end='\n')