def solution(nn):
    a = []
    b = []

    for i in range(len(nn)):
        a.append(max(nn[i]))
        b.append(min(nn[i]))

    return max(a) * max(b)
    

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))


# 둘이 값 바꾸는거 한줄
# a, b = b, a

#다른사람 풀이
# return max(max(x) for x in sizes) * max(min(x) for x in sizes)
