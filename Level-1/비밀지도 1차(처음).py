def solution(n, arr1, arr2):

    #최종 지도 리스트 
    result = []

    #공통 함수 생성
    def arr_2(nn, arr):
        List = []

        for j in arr:
            test = []
            while j > 0:
                test.append(j % 2)
                j //= 2
            test.reverse()

            if len(test) != nn:
                count = nn - len(test)
                for i in range(count):
                    test.insert(i, 0)
            
            List.append(test)

        return List

    #함수 실행
    aList = arr_2(n, arr1)
    bList = arr_2(n, arr2)

    #두 개 공통점 확인하여 리스트 생성
    for i in range(n):
        test_result = ''
        for j in range(n):
            if aList[i][j] == 0 and bList[i][j] == 0:
                test_result += ' '
            else:
                test_result += '#'
        result.append(test_result)


    return result

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(5, [9, 20, 28, 18, 11]))



