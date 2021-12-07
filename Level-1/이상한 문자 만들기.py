#첫 시도
# def solution(s):
#     s = list(s.split(" "))
#     result = ''
#     for i in range(len(s)):
#         for j in range(len(s[i])):
#             if j % 2 == 0:
#                 result += s[i][j].upper()
#             else:
#                 result += s[i][j] 
#         result += ' '
#     return result
# print(solution("try hello world"))


#두 번째 시도
# def solution(s):
#     s = list(s.split(" "))
#     for i in range(len(s)):
#         for j in range(len(s[i])):
#             if j % 2 == 0:
#                 s[i] = s[i].replace(s[i][j], s[i][j].upper())
#             else:
#                 s[i] = s[i].replace(s[i][j], s[i][j].lower())
               
#     return " ".join(s)

# print(solution("try hello world"))


# a = 'asda'
# a = a.replace('a', '12')
# print(a)



#결국 정답
def solution(s):
    answer = []
    s = s.split('')

    for i in range(len(s)):
        result = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                result += s[i][j].upper()
            else:
                result += s[i][j].lower()

        answer.append(result)

    return ' '.join(answer)



#다른사람 풀이
# def solution(s):
#     return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))