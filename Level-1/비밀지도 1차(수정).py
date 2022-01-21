def solution(n, arr1, arr2):

    result = []

    for i in range(n):
        a = arr1[i] | arr2[i]
        temp =''

        for j in range(n):    
            if a % 2 == 0:
                temp = ' ' + temp
            else:
                temp = '#' + temp
            a //= 2

        result.append(temp)
    
    return result

        

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(5, [9, 20, 28, 18, 11]))



