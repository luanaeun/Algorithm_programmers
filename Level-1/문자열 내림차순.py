def solution(s):
    s = list(s)
    s.sort(reverse=True)
    s = "".join(s)
    return s



def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution("Zbcdefg"))