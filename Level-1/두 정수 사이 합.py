# min, max 활용
# def solution(a, b):
#     result = sum([i for i in range(min(a,b), max(a,b)+1)])
#     return result


def solution(a, b):
    a = range(a, b+1)
    print(a)
    #result = sum(range(min(a,b), max(a,b)+1))
    #return result

print(solution(3, 3))