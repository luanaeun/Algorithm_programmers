a = "1e22"

def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    else:
        return False



def solution(s):
    length = len(s)
    
    if not (length == 4 or length == 6):
        return False
    else:
        if s.isdigit():
            return True
        else:
            return False


def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

print(solution(a))