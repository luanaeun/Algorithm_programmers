# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

# 런타임 에러...... => ZeroDivisionError: division by zero 에러
def solution(n, arr):
    res = {}
    for i in range(1, n+1):
        res[i] = arr.count(i) / len(arr)
        remove_set = {i}
        arr = [j for j in arr if j not in remove_set]


    res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
    
    return list(res.keys())



# if len(arr) == 0: 을 추가해 위 코드의 에러를 없앴다. 

def solution(n, arr):
    res = {}
    for i in range(1, n+1):
        if len(arr) == 0:
            res[i] = 0
        else:
            res[i] = arr.count(i) / len(arr)
            remove_set = {i}
            arr = [j for j in arr if j not in remove_set]

    res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
    
    return list(res.keys())


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(5, [2,1,2,4,2,4,3,3]))


# 리스트 내의 특정 요소 모두 제거하기
# li = [1, 3, 5, 5, 7, 7, 8]
# remove_set = {3, 5}

# li = [i for i in li if i not in remove_set]
# print(li)


