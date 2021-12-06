def solution(n, m):
    answer = []
    beasu = n*m
    yaksu = 0
    for i in range(2, m+1):
        if n%i == 0 and m%i == 0:
            yaksu = i
        elif yaksu == 0:
            yaksu = 1
    answer.append(yaksu)

    for i in range(beasu, 1, -1):
        if i%n == 0 and i%m == 0 and i<beasu:
                beasu = i
    answer.append(beasu)

    return answer



#다른사람 풀이
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

#최대공약수 구하는 법: (두 수 중 작은 수) 나누기 (두 수를 나눈 나머지)를 반복하여 나머지가 0이될때의 값. 
#최소공배수 구하는 법: (두 수의 곱) 나누기 (최대공약수) 