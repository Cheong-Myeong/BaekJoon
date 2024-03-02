N = int(input())
lst = []
for _ in range(N):
    age, name = map(str, input().split())
    lst.append([int(age), name])
final_lst = sorted(lst, key=lambda x: x[0])  # 나이로 오름차순 정렬
                          # 나이 같으면 순서 안 바뀌어서 가입 순 그대로
for age, name in final_lst:
    print(f'{age} {name}')