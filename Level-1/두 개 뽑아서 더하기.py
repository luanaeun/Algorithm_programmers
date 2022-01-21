def solution(arr):
    result = []

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            result.append(arr[i] + arr[j])
    
    result = sorted(list(set(result)))
    
    return result


print(solution([0,7,2,7]))