def solution(d, budget):
    answer = 0
    acc = 0
    for cost in sorted(d):
        acc += cost
        if (acc > budget):
            return answer

        answer += 1

    return answer
        