def solution(n):
    a = 0
    for i in str(n):
        a += int(i)
    result = n % a

    if result == 0:
        return True
    else:
        return False



print(solution(123))