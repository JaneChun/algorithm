def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1] # 끝까지 비교했을 때 차이가 없으면 마지막 참가자가 완주하지 못한 사람
        
    # for comp in completion:
    #     if comp in participant:
    #         participant.remove(comp)
    # return participant[0]