import math

#시간초과로 실패.
# def solution(n):
#     result = 0
#     for i in range(1, n+1):
#         count = 0
#         for j in range(1, i//2+1):
#             if i%j == 0:
#                 count += 1

#         if count == 1:
#             result += 1
    
#     return result

# print(solution(10))


#시간초과+효율성 실패
# def solution(n):
#     result = 0
#     for i in range(1, n+1, 2):
#         count = 0
#         for j in range(1, int(math.sqrt(i))+1):
#             if i%j == 0:
#                 count += 1

#         if count == 1:
#             result += 1
    
#     return result

# print(solution(10))



def solution(n):
    a = [True] * (n+1)
    print(a)

    for i in range(2, n//2+1):
        if a[i] == True:           
            for j in range(i+i, n+1, i):
                a[j] = False
        print(a)

    # 소수 목록 산출
    return len([i for i in range(2, n+1) if a[i] == True])

print(solution(10))



#다른사람 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)





