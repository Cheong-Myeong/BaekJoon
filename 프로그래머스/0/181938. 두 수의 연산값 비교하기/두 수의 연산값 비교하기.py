def solution(a, b):
    num1 = str(a) + str(b)
    num2 = str(b) + str(a)
    if int(num1) < 2*a*b:
        answer = 2*a*b
    elif int(num1) > 2*a*b:
        answer = int(num1)  
    else:
        answer = int(num1)      
    return answer