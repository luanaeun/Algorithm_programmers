def solution(s, n):
    
    result = []

    a = sorted([i[n] for i in s])
    print(a)

    for i in a:
        for j in s:
            if i == j[n]:
                result.append(j)
    
    result = list(set(result))
    return result

# def solution(strings, n):
#     return sorted(strings, key=lambda x: x[n])


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))

