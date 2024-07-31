from collections import Counter

def string_to_dict(s):
    return dict(Counter(s))

def solution(X, Y):
    X_dict = string_to_dict(X)  # {'1': 2, '2': 2, '3': 1}
    Y_dict = string_to_dict(Y)
    
    result = ''
    
    for i in range(9, -1, -1): # 9 ~ 0 순회
        key = str(i)
        minCount = min(X_dict.get(key, 0), Y_dict.get(key, 0)) # get()으로 접근하여 KeyError 방지
        result += key * minCount
    
    if not len(result):
        return "-1"
    elif result[0] == '0':
        return "0"
    else:
        return result
        
