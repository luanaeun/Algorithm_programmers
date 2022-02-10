# 효율성 실패
# def solution(participant, completion):
#     for i in completion:
#             participant.remove(i)

#     return participant[0]  

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


print(solution(
    ["marina", "josipa", "nikola", "vinko", "filipa"], 
    ["josipa", "filipa", "marina", "nikola"]
))

print(solution(
    ["mislav", "stanko", "mislav", "ana"],
    ["stanko", "ana", "mislav"]
))

print(solution(
    ['A', 'B', 'C', 'D', 'E'],
    ['A', 'B', 'D', 'E']
))