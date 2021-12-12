def solution(s):
    if len(s) <= 50 and s.isalpha():
        s = s.lower()
        return s.count('p') == s.count('y')

    else:
        return False



print(solution("Pyy"))