def solution(n):
    result=""
    for i in range(n):
        if i%2 == 0:
            result += "수"
        else:
            result += "박"
    return result

print(solution(3))


#다른사람 풀이
# def solution(n):
#     print("수박" * int(n/2) + "수" if n % 2 else "수박" * int(n/2))
#     return ("수박"*n)[0:n]


