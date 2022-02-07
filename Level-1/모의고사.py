def solution(answer):

    rules = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = []
    max_n = 0

    for r in range(len(rules)):
        count = 0
        total = 0
        for i in answer:
            # print("정답:", i)
            # print("규칙: ", rules[r][count])
            
            if i == rules[r][count]:
                total += 1

            if count == len(rules[r])-1:
                count = -1

            count += 1
        
        
        if total >= max_n:
            if total > max_n:
                result = []
            max_n = total
            result.append(r+1)


    return result

#print(solution([3, 3, 2, 1, 5]))

print(solution([1, 2, 3, 4, 5]))
# print(solution([1,3,2,4,2]))
# print(solution([0,0,0,0,0]))

# 1번 테케
print(solution([1, 1, 1, 1]))

# 1, 3번둘다 max일 경우
print(solution([9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5]))