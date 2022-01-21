def solution(n):
    result = []
    res = 0

    while (n > 0):
        result.append(n%3)
        n //= 3

    l = len(result)

    for i in range(l):
        res += result[i] * (3**(l-1-i))

    return res    

print(solution(45))


# 새로 배운 것.
# int(값, 진수) 를 넣으면 해당 진법으로 변경한다. 