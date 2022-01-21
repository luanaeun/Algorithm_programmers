def solution(s):
    a = []
    answer = []

    for i in range(len(s)):
        if s[i] == '1' and s[i+1] == '0':
            a.append(10)
        elif s[i-1] == '1' and s[i] == '0':
            continue
        else:
            a.append(s[i])

    for i in range(len(a)):
        if a[i] == 'S':
            answer.append(int(a[i-1]))
        elif a[i] == 'D':
            answer.append(int(a[i-1])**2)
        elif a[i] == 'T':
            answer.append(int(a[i-1])**3)

        if a[i] == '*':
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif a[i] == '#':
            answer[-1] *= -1
        print(answer)
    print(answer)
    return sum(answer)


#print(solution('2D*1S#5S#'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# print(solution('1S*2T*3S'))
# print(solution('1D#2S*3S'))
# print(solution('1T2D3D#'))
print(solution('1D2S3T*'))



#i.isdigit():
#isalpha()


