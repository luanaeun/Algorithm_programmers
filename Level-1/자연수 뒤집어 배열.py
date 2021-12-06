def solution(n):  
    result = []    
    n = list(str(n))
    for i in range(len(n)-1, -1, -1):
        result.append(int(n[i]))

    return result

print(solution(12345))


def digit_reverse(n):
    return list(map(int, reversed(str(n))))


    
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)))



def digit_reverse(n):
    # 함수를 완성해 주세요
    ret =[]
    for i in str(n):
        ret.append(int(i))
    ret.reverse() 
    return ret

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)))