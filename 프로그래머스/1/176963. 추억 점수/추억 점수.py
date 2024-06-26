def solution(name, yearning, photo):
    answer = []
    zipped = dict(zip(name, yearning))
    
    for nameArr in photo:
        sumOfYearning = 0
        for name in nameArr:
            sumOfYearning += zipped.get(name, 0)
            # zipped[name] 사용 시 키가 없는 경우 keyError 반환
            # dict.get() 사용 시 키가 없으면 0을 반환하도록 기본값 지정 가능
        answer.append(sumOfYearning)
    
    return answer