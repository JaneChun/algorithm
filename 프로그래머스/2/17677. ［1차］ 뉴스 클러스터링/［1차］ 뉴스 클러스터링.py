from collections import Counter

def solution(str1, str2):     
    # 2자리씩 끊기
    arr1 = makeArr(str1)
    arr2 = makeArr(str2)
    
    # 원소 개수 계산
    counter1 = {}
    counter2 = {}
    
    for item in arr1:
        counter1[item] = counter1.get(item, 0) + 1
        
    for item in arr2:
        counter2[item] = counter2.get(item, 0) + 1
        
    # 교집합 계산 (각 원소의 최소 빈도 합산)
    inter = 0
    for key in counter1:
        if key in counter2:
            inter += min(counter1[key], counter2[key])
            
    # 합집합 계산 (각 원소의 최대 빈도 합산)
    union = 0
    unique_keys = set([*list(counter1.keys()), *list(counter2.keys())])

    for key in unique_keys:
        union += max(counter1.get(key, 0), counter2.get(key, 0))
            
    answer = 1 if inter == 0 and union == 0 else inter / union
    
    return int(answer * 65536)    

def makeArr(str):
    arr = []
    for i in range(0, len(str)):
        word = str[i:i+2]
        if len(word) == 2 and word.isalpha():
            arr.append(word.lower())
    return arr