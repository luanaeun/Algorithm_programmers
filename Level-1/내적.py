def solution(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result
  
a = [1,2,3,4]
b = [-3,-1,0,2]

# a = [-1, 0, 1]
# b = [1, 0, -1]

print(solution(a, b))
