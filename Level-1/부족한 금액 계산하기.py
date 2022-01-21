def solution(p, m, c):
  
    total = sum([p*i for i in range(1, c+1)])
        
    if total > m:
        return total -m
    else:
        return 0



def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)


print(solution(3, 20, 4))


# 1 ~ n 까지 더한 수는 (n+1) * n / 2 와 같다. 
# 반복문 돌릴 필요없이 price*(count+1)*count/2 로 나타낼 수 있다. 
# 