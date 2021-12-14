def solution(arr, d):

    result = sorted([i for i in arr if i %d == 0])

    if len(result) == 0:
        return [-1]
    else:
        return result


# # 더 간단히(2줄)
# def solution(arr, d):

#     result = sorted([i for i in arr if i %d == 0])

#     return result if len(result) != 0 else [-1]


# 더 간단히(1줄)
# def solution(arr, d):

#     return sorted([i for i in arr if i %d == 0]) or [-1]



print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))