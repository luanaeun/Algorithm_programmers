# def solution(n):
#     a = [True] * (n+1)
#     print(a)

#     for i in range(2, n//2+1):
#         if a[i] == True:           
#             for j in range(i+i, n+1, i):
#                 a[j] = False
#     print("판별에이", a)

#     # 소수 목록 산출
#     return len([i for i in range(2, n+1) if a[i] == True])

# print(solution(10))


def solution(a, b):
    return a+b

print(solution(9223372036854775807, 9223372036854775808))