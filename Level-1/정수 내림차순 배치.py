def solution(n):
    n = list(str(n))
    n.sort(reverse = True)
    
    return int("".join(n))

print(solution(118372))


#sort()함수 없이 풀어봄.
def solution(n):
    n = list(str(n))

    for i in range(len(n)-1):
        for j in range(0, len(n)-1):
            if n[j] < n[j+1]:
                c = n[j+1]
                n[j+1] = n[j]
                n[j] = c
        print(n)
    return int(''.join(n))