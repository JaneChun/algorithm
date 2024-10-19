# 백트래킹: 문제를 해결하기 위해 가능한 모든 해를 탐색하는 방식
# 재귀적으로 후보 해를 만들어 가며, 그 후보 해가 조건에 맞지 않을 경우에는 그 자리에서 중단하고 이전 단계로 돌아가 다른 경로를 탐색하는 방식

from itertools import permutations

def solution(k, dungeons):
    result = []
    permutation = permutations(dungeons) # 탐험 가능한 모든 경우의 수(순열)를 구함
    
    for p in permutation:
        answer = explore(k, p)
        result.append(answer)
    
    return max(result)
    
    
def explore(k, dungeons):
    answer = 0
    curFatigue = k
    for requiredFatigue, consumedFatigue in dungeons:
        if curFatigue >= requiredFatigue:
            answer += 1
            curFatigue -= consumedFatigue
    return answer