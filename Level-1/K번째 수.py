def solution(arr, commands):
    result = []

    for com in commands:
        start = com[0]-1
        end = com[1]

        new_com = sorted(arr[start:end])
        result.append(new_com[com[2]-1])
    return result



print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))