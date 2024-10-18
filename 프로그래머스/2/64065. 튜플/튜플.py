def solution(s):
    arr = s[1:-1].strip('{}').split('},{')
    
    countSet = {}
    for string in arr:
        elements = string.split(',')
        for el in elements:
            # 해당 키가 없으면 기본값 0을 반환하고 1을 더함
            countSet[el] = countSet.get(el, 0) + 1
            
    sortedDict = sorted(countSet.items(), key=lambda item: item[1], reverse=True)
    
    return [int(key) for key, value in sortedDict]