# 리스트 활용
# def solution(a, b):
#     result = sum([i for i in range(min(a,b), max(a,b)+1)])
#     return result


def solution(a, b):
 
    result = sum(range(min(a,b), max(a,b)+1))
    return result

print(solution(3, 3))


# a,b 동시에 바꾸려면?
#a, b = b, a