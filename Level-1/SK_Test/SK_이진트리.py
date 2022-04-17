def solution(n, clockwise):
    answer = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
             ]
    a = 1
    
    count = 0

    for i in range(4):

        if count == 0:
            for i in range(n-1):
                answer[0][i] = a
                a += 1
            count = 2
            a = 1

        if count == 1:
            for i in range(n-1):
                answer[i][4] = a
                a += 1
            a = 1
    

    print(answer)


    

print(solution(5, True))