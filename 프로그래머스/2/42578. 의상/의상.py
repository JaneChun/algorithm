def solution(clothes):
    answer = 0
    types = set()
    
    types = {t for [_, t] in clothes} # {'eyewear', 'headgear'}
    type_dict = {t: [] for t in types}
    # {'eyewear': [], 'headgear': []}
    
    for [n, t] in clothes:
        type_dict[t].append(n)
    # 	{'eyewear': ['blue_sunglasses'], 'headgear': ['yellow_hat', 'green_turban']}    
    
    answer = 1
    for arr in type_dict.values():
        answer *= (len(arr) + 1)

    return answer - 1 