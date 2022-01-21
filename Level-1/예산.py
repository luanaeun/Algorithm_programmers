# def solution(d, budget):
#     d = sorted(d)
#     result = 0

#     if sum(d) <= budget:
#         return len(d)

#     else:
#         for i in range(len(d)):
#             result += d[i]

#             if result > budget:
#                 return i
        
def solution(d, budget):
    d.sort()
    result = 0
    cnt = 0

    for i in d:
        result += i

        if result > budget:
            return cnt       
        cnt += 1

    return cnt




print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))
print(solution([3], 5))
