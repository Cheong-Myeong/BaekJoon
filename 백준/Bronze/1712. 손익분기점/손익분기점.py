A, B, C = map(int, input().split())  # 고정 비용, 가변 비용, 노트북 가격
# 손익분기점 x 계산 방법 = A + Bx < Cx
if C - B <= 0:
    print(-1)
else:
    break_even_point = A // (C - B)  # 비용과 노트북 판매량이 같을 때
    print(break_even_point+1)        # +1 출력