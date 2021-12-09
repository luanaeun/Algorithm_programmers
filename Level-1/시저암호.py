alpa = "abcdefghijklmnopqrstuvwxyz"

def solution(s, n):
    result = ''
    for i in range(len(s)):
        if s[i] == ' ':
            result += ' '
        else:
            a = alpa.index(s[i].lower())

            if a+n > 25:
                b = a+n-26
            else:
                b = a+n

            if s[i].isupper():
                result += alpa[b].upper()
            else:
                result += alpa[b]

    return result

print(solution("a B z", 4))



#다른사람 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)