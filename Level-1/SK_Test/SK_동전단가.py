# 동전의 단가를 계산하는 문제

def solution(money, costs):
    costs.reverse()
    dongen = [500, 100, 50, 10, 5, 1]
    print(costs)

    answer = 0

    for i in range(len(costs)-1):
        print("머니: ", money)
        print("동전: ", dongen[i])
        if money < 5:
            print("1의자리 단가: ", costs[i+1] * money)
            answer += (costs[i+1] * money)
        if money >= dongen[i]:
            print("동전뭐로 계산?", dongen[i])
            diff_dongen = dongen[i] / dongen[i+1]
            diff_costs = costs[i] / costs[i+1]
            print("동전 차이: ", diff_dongen)
            print("단가 차이: ", diff_costs)
            
            if(diff_dongen >= diff_costs):
                answer += (costs[i] * (money // dongen[i]))
                money %= dongen[i]
            else:
                answer += (costs[i+1] * (money // dongen[i+1]))
                money %= dongen[i+1] 
        
    return answer

print()
# print(solution(4578, [1, 4, 99, 35, 50, 1000]))
print(solution(1999, [2, 11, 20, 100, 200, 600]))