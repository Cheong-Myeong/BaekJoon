# 아파트 거주민 수를 저장할 2차원 배열 생성 및 초기화
apartment = [[0] * 15 for _ in range(15)]
for i in range(15):
    apartment[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        # 이전 층의 해당 호수까지의 거주민 수의 합을 구함
        apartment[i][j] = apartment[i][j - 1] + apartment[i - 1][j]

# 테스트 케이스 수 입력
T = int(input())
for _ in range(T):
    # 층수와 호수 입력
    k = int(input())
    n = int(input())
    # 해당 층, 해당 호수의 거주민 수 출력
    print(apartment[k][n])