def solution(arr):
    result = [arr[0]]
    a = arr[0]

    for i in arr:
        if i != a:
            result.append(i)
            a = i

    return result


# 다른사람 풀이
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a



print(solution([1,1,3,3,0,1,1]))