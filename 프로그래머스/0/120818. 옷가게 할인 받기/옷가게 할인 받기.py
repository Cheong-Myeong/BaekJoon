def solution(price):
    if price >= 100000 and price < 300000:
        price *= 0.95
    if price >= 300000 and price < 500000:
        price *= 0.90
    if price >= 500000:
        price *= 0.80
    answer = int(price)
    return answer