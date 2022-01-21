def solution(a, b):
    res = 0
    for i in range(a, b+1):
        
        cnt = len([j for j in range(1, i//2+1) if i%j == 0]) +1
    
        if cnt%2 == 0:
            res += i
        else:
            res -= i

    return res

print(solution(13, 17))
print(solution(24, 27))


# 약수가 홀수개인 모든 수는 제곱수이다. 
# 다른사람 풀이
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer
