
def solution(n):
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            a.append(i)
    print(a)
   
    return sum(a)
    

# 위의 코드 한 줄 작성
def solution(n):
    return sum([i for i in range(1, n+1) if n%i==0])


#다른사람 풀이 
def other_solution(num):   
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])



print(solution(4))