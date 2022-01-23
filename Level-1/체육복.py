def solution(n, lost, reserve):

    # 두 리스트의 중복 제거
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))

    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)

    return n - len(new_lost)



# 결과 확인을 위한 출력코드
print(solution(5, [2, 4], [1, 3, 5])) #5
print(solution(5, [2, 4], [3])) #4
print(solution(3, [3, 4], [1, 4])) #2
print(solution( 9, [5,6,8,1,2], [2,3,1,4,8,9 ] )) #8
print(solution( #30
        30,
        [1, 2, 7, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27], # 16개
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 23, 24, 25, 26, 27, 28], # 25개
    ))
print(solution(7, [3, 5, 6], [4, 1, 6])) #6
print(solution(4, [3, 1], [2, 4])) #4

#테스트 케이스 5번
print(solution(5, [2, 3, 4], [1, 2, 3] )) 